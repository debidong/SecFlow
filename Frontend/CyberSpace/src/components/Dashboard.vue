<script>
import axios from 'axios';

export default {
    data() {
      return {
        uid: '',
        username: '',
        loaded: false,
        config: {},
        // Reminder module
        reminder: [],
        topic: '',

        friends: [],
        inbox: []
      }
    },
    methods: {
      getToken() {
        this.config = {
          headers: {
            'token': localStorage.getItem('token')
          }
        }
      },

      requireGET(url) {
        var url_ = 'api/user/dashboard/' + url;
        return axios.get(url_, this.config)
        .then((response) =>
          response.data
        )
      },

      requirePOST(url, params) {
        var url_ = 'api/user/dashboard/' + url;
        return axios.post(url_, params, this.config).then(
          (response) => response.data
        )

      },

      getUserInfo() {
        this.requireGET('info').then((data) => {
          this.uid = data['uid']; 
          this.username = data['username'];
        }).catch(error => {
          if(error.response.status == 401) {
            this.$router.push('/login')
          }
        });
      },

      /* Module: Reminder */
      getUserReminder() {
        this.requireGET('reminder').then((data) => {
          this.reminder = data['reminder'];
        }).catch(error => {
          if(error.response.status == 401) {
            this.$router.push('/login')
          }
        });
      },
      handleReminder(topic, action) {
        var params = {
          'topic': topic,
          'action': action
        }
        this.requirePOST('reminder', params).then((data) => {
            if(action == 'add') {
              this.topic = '';
            }
          this.getUserReminder();
        }).catch(error => {
          if(error.response.status == 401) {
            this.$router.push('/login')
          }
        });
      },

      /* Module: Friends */
      getUserFriends() {
        this.requireGET('friends').then((data) => {
          this.friends = data['friends'];
        }).catch(error => {
          if(error.response.status == 401) {
            this.$router.push('/login')
          }
        });
      },


      handleFriendRequest(sender, anwser) {
        var params = {
          'sender': sender,
          'anwser': anwser
        };
        this.requirePOST('userList/friendRequest/handle', params).then((data) => {
          this.getUserInbox();
          this.getUserFriends();
        })
      },

      /* Module: Inbox */
      getUserInbox() {
        this.requireGET('inbox').then((data) => {
            this.inbox = data['inbox'];
        }).catch(error => {
          if(error.response.status == 401) {
            this.$router.push('/login')
          }
        });
      },


      goToChatroom(uid, username) {
        let token = localStorage.getItem('token');
        let params = {
          'myUid': this.uid,
          'myUsername': this.username,
          'uid': uid,
          'username': username
        };
        let config = {
          headers: {
            'token': token,
          }
        };
        axios.post('api/chat/chatroom', params, config).then((response) => {
            let params = {
              'myUid': this.uid,
              'myUsername': this.username,
              'uid': uid,
              'username': username,
              'rid': response.data['rid']
            };

            this.$store.commit('setRoomInfo', params);
            this.$router.push('/chat');
        }).catch(error => {
          if(error.response.status == 401) {
            this.$router.push('/login')
          }
        });
      },

      logout() {
        let url = 'api/accounts/' + this.uid
        axios.delete(url, this.config).then(response => {
          this.$router.push('/')
        })
      },

      deleteAccount() {
        let url = 'api/accounts/' + this.uid
        axios.delete(url, this.config).then(response => {
          this.$router.push('/')
        })
      }
    },

    mounted() {
      this.getToken();
      this.getUserInfo();
      this.getUserReminder();
      this.getUserFriends();
      this.getUserInbox();
    }
}
</script>


<template>
    <el-container>
        <el-header>
            <h1>
                Dashboard
            </h1>

        </el-header>
        <el-main>
            <el-row :gutter="10">
                <el-col :span="6" />
                <el-col :span="12">
                    <el-breadcrumb>
                    <el-breadcrumb-item :to="{ path: '/' }">Home</el-breadcrumb-item>
                    <el-breadcrumb-item :to="{ path: '/dashboard' }">Dashboard</el-breadcrumb-item>
                    </el-breadcrumb>                    
                </el-col>
                <el-col :span="6" />
            </el-row>
            <el-row :gutter="10">
                <el-col :span="6" />
                <!-- left column -->
                <el-col id="left-side" :span="6">
                    
                    <!-- personal info -->
                    <el-card class="box-card1">
                        <template #header>
                        <div class="card-header1">
                            <span>Hi {{ username }}</span>
                            <el-button size="default" @click="$router.push({path: '/userlist'})" text>Info</el-button>
                        </div>
                        </template>
                        <div>
                            <el-tag effect="plain" size="large">Uid</el-tag> {{ uid }}
                            <br>
                            <el-tag effect="plain" size="small">Username</el-tag> {{ username }}
                        </div>
                    </el-card>
                    <!----- FRIENDS ----->
                    <el-card class="box-card1">
                        <template #header>
                        <div class="card-header1">
                            <span>Friends</span>
                            <div>
                                <el-button size="default" @click="$router.push({path: '/userlist'})" text>Find</el-button>
                            </div>
                        </div>
                        </template>
                        <div>
                            <div v-for="i in friends">
                                <el-card class="box-card2">
                                    <template #header>
                                        <div class="card-header2">
                                            {{ i.username }}
                                            <div>
                                                <el-button type="success" @click="goToChatroom(i.username, i.uid)">Chat</el-button>
                                                <el-button type="info">Manage</el-button>
                                            </div>
                                        </div>
                                    </template>
                                    <el-tag size="small">Uid</el-tag>{{ i.uid }}<br>
                                </el-card>
                            <!-- <el-button type="info" size="small" @click="del_remind(i)">Done</el-button> -->
                            </div>
                        </div>
                    </el-card>
                    <!-- groups -->
                    <!-- <el-card class="box-card1">
                        <template #header>
                        <div class="card-header1">
                            <span>Groups</span>
                        </div>
                        </template>
                        <div>
                            Under construction
                        </div>
                    </el-card> -->
                </el-col>
            
                <!-- right column -->
                <el-col id="right-side" :span="6">
                    <!----- INBOX ----->
                    <el-card class="box-card1">
                        <template #header>
                        <div class="card-header1">
                            <span>Inbox</span>
                            <el-button size="default" @click="getUserInbox" text>Refresh</el-button>
                        </div>
                        </template>
                        <div v-for="msg in inbox" :key="friend_request">
                            <div v-for="(key, value) in msg">
                                <el-card class="box-card2">
                                    <template #header>
                                        <div class="card-header2">
                                            <span>Friend Request</span>
                                            <div>
                                                    <el-button type="success" @click="handleFriendRequest(value, 'agree')">Agree</el-button>
                                                    <el-button type="danger" @click="handleFriendRequest(value), 'refuse'">Reject</el-button>
                                                
                                            </div>
                                        </div>
                                    </template>
                                    <span>Uid: {{ value }}</span><br>
                                    <span>Username: {{ key }}</span>                                  
                                </el-card>
                            </div>  
                        </div>
                    </el-card>
                    <!----- REMINDER ----->
                    <el-card class="box-card1">
                        <template #header>
                        <div class="card-header1">
                            <span>Reminder</span>
                            <el-button size="default" @click="handleReminder(this.topic, 'add')" text>Add</el-button>
                        </div>
                        </template>
                        <div>
                            <el-input v-model="topic" placeholder="Any topic" />
                        </div>
                        <div v-for="i in reminder">
                            <el-card class="box-card2">
                                <span>{{ i }}</span>
                                <div id="button-on-right">
                                    <el-button type="success" size="small" @click="handleReminder(i, 'delete')">Done</el-button>
                                </div>
                            </el-card>
                        </div>
                    </el-card>
                    <el-card class="box-card1">
                        <template #header>
                        <div class="card-header1">
                            <span>Settings</span>
                        </div>
                        </template>
                        <div>
                            <el-button id="button" type="warning" size="default" @click="logout">Logout</el-button>
                            <br>
                            <el-button id="button" type="info" size="default" @click="change_password">Change Password</el-button>
                            <br>
                              <el-popover
                              id="button"
                              trigger="click"
                              placement="top"
                              :width="fit-content">
                              <el-text type="danger" id="button" tag="p">All your data will be deleted irreversibly.</el-text>
                              <el-text type="danger" id="button" tag="p">Continue?</el-text>

                              <!-- <p>All your data will be deleted irreversibly.</p>
                              <p>Continue?</p> -->
                              <el-button id="button" size="default" type="danger" @click="deleteAccount">Confirm</el-button>
                              <template #reference>
                              <el-button id="button" type="danger" size="default">Delete Account</el-button>
                              </template>
                            </el-popover>
                        </div>
                    </el-card>
                </el-col>
            </el-row>            
        </el-main>
    </el-container>

    
</template>

<style scoped>
.el-header {
    position: relative;
    text-align: center;
    justify-content: center;
    font-size: x-large;
    margin-bottom: 10%;
}
.card-header1 {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: larger;
  font-weight: bold;
}

.card-header2 {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: medium;
    font-weight: bold;
}

.left-side {
    width: 30%;
    margin: 0;
    margin-left: 0%;
    margin-right: 0%;
}

.right-side {
    width: 30%;
    margin: 0;
    margin-right: 0%;
    margin-top: 1%; 
}

.box-card1 {
    font-size: large;
    margin-top: 3%;
}

.box-card2 {
    font-size: small;
    position: relative;
    margin-top: 1%;
    margin-bottom: 1%;
}

#button-on-right {
    float: right;
}

#button {
    width: 100%;
    margin: auto;
    margin-bottom: 1%;
}
</style>