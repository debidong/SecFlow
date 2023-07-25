<script>
import axios from 'axios';

export default {
    data() {
        return {
            uid: '',
            username: '',
            loaded: false,

            // Reminder module
            reminder: [],
            topic: '',

            friends: [],
            inbox: []
        }
    },
    methods: {
        requireGET(url) {
            var token = localStorage.getItem('token');
            var config = {
                headers: {
                    'token': token,
                }
            };
            var _url = 'api/user/dashboard/' + url;
            return axios.get(_url, config)
            .then((response) =>
                response.data
            )
        },

        requirePOST(url, params) {
            var token = localStorage.getItem('token');
            var config = {
                headers: {
                    'token': token,
                }
            };
            var _url = 'api/user/dashboard/' + url;
            return axios.post(_url, params, config).then(
                (response) => response.data
            )

        },

        getUserInfo() {
            this.requireGET('info').then((data) => {
                this.uid = data['uid']; 
                this.username = data['username'];
            });

        },

        /* Module: Reminder */
        getUserReminder() {
            this.requireGET('reminder').then((data) => {
                this.reminder = data['reminder'];
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
            })
        },

        /* Module: Friends */
        getUserFriends() {
            this.requireGET('friends').then((data) => {
                this.friends = data['friends'];
            })
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
            })
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
                })
        }
    },

    mounted() {
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
            <el-breadcrumb :separator-icon="ArrowRight">
            <el-breadcrumb-item :to="{ path: '/' }">Home</el-breadcrumb-item>
            <el-breadcrumb-item :to="{ path: '/dashboard' }">Dashboard</el-breadcrumb-item>
            </el-breadcrumb>
            <el-row :gutter="10">
                <!-- left column -->
                <el-col id="left-side" :span="12">
                    <!-- personal info -->
                    <el-card class="box-card1">
                        <template #header>
                        <div class="card-header1">
                            <span>Hi {{ username }}</span>
                        </div>
                        </template>
                        <div>
                            <el-tag size="small">Uid</el-tag> {{ uid }}
                            <br>
                            <el-tag size="small">Username</el-tag> {{ username }}
                        </div>
                    </el-card>
                    <!----- FRIENDS ----->
                    <el-card class="box-card1">
                        <template #header>
                        <div class="card-header1">
                            <span>Friends</span>
                            <div>
                                <el-button type="info" size="medium" @click="$router.push({path: '/userlist'})">Find</el-button>
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
                    <el-card class="box-card1">
                        <template #header>
                        <div class="card-header1">
                            <span>Groups</span>
                        </div>
                        </template>
                        <div>
                            pass
                        </div>
                    </el-card>
                </el-col>
            
                <!-- right column -->
                <el-col id="right-side" :span="12">
                    <!----- INBOX ----->
                    <el-card class="box-card1">
                        <template #header>
                        <div class="card-header1">
                            <span>Inbox</span>
                            <el-button type="info" size="medium" @click="getUserInbox">Refresh</el-button>
                        </div>
                        </template>
                        <div v-for="msg in inbox" :key="friend_request">
                            <div v-for="(key, value) in msg">
                                <el-card class="box-card2">
                                    <template #header>
                                        <div class="card-header2">
                                            <span>Friend Request</span>
                                            <div>
                                                <el-button type="success" @click="handleFriendRequest(value, 'agree')"></el-button>
                                                <el-button type="danger" @click="handleFriendRequest(value), 'refuse'"></el-button>
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
                            <el-button type="info" size="medium" @click="handleReminder(this.topic, 'add')">Add</el-button>
                        </div>
                        </template>
                        <div>
                            <el-input v-model="topic" placeholder="Things to remind" />
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
                            <el-button type="warning" size="medium" @click="logout">Logout</el-button>
                            <br>
                            <el-button type="info" size="medium" @click="change_password">Change Password</el-button>
                            <br>
                
                            <el-button type="danger" size="medium" @click="delete_account">Delete Account</el-button>
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
</style>