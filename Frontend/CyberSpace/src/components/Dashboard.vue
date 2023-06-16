<script>
import axios from 'axios';
axios.defaults.baseURL = 'http://127.0.0.1:8000'

export default {
    data() {
        return {
            uid: '',
            username: '',
            loaded: false,

            reminder: [],
            to_remind: '',

            friends: [],
            inbox: []
        }
    },
    methods: {
        require_get(url) {
            var token = localStorage.getItem('token');
            var config = {
                headers: {
                    'token': token,
                }
            };
            var _url = 'user/dashboard/' + url;
            return axios.get(_url, config)
            .then((response) =>
                response.data
            )
        },

        require_post(url, param) {
            var token = localStorage.getItem('token');
            var config = {
                headers: {
                    'token': token,
                }
            };
            var _url = 'user/dashboard/' + url;
            return axios.post(_url, param, config).then(
                (response) => response.data
            )

        },

        get_user_info() {
            this.require_get('info').then((data) => {
                this.uid = data['uid']; 
                this.username = data['username'];
            });

        },

        /* Module: Reminder */
        get_user_reminder() {
            this.require_get('reminder').then((data) => {
                this.reminder = data['reminder'];
            });
        },
        send_remind() {
            var param = {
                'topic': this.to_remind
            }
            this.require_post('reminder/add', param).
            then(this.get_user_reminder);
            this.to_remind = '';
        },
        del_remind(i) {
            var param = {
                'topic': i
            };
            this.require_post('reminder/delete', param).
            then(this.get_user_reminder);
        },

        /* Module: Friends */
        get_user_friends() {
            this.require_get('friends').then((data) => {
                this.friends = data['friends'];
            })
        },


        agree_friend_request(sender) {
            var param = {
                'sender': sender,
                'anwser': 'agree'
            };
            this.require_post('userList/friendRequest/handle', param).then((data) => {
                this.get_user_inbox();
                this.get_user_friends();
            })
        },


        refuse_friend_request(sender) {
            var param = {
                'sender': sender,
                'anwser': 'refuse'
            };
            this.require_post('userList/friendRequest/handle', param).then((data) => {
                this.get_user_inbox();
                this.get_user_friends();
            })
        },

        /* Module: Inbox */
        get_user_inbox() {
            this.require_get('inbox').then((data) => {
                this.inbox = data['inbox'];
            })
        }
    },

    mounted() {
        this.get_user_info();
        this.get_user_reminder();
        this.get_user_friends();
        this.get_user_inbox();
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
                                                <el-button type="success">Chat</el-button>
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
                            <el-button type="info" size="medium" @click="get_user_inbox">Refresh</el-button>
                        </div>
                        </template>
                        <div v-for="msg in inbox" :key="friend_request">
                            <div v-for="(key, value) in msg">
                                <el-card class="box-card2">
                                    <template #header>
                                        <div class="card-header2">
                                            <span>Friend Request</span>
                                            <div>
                                                <el-button type="success" @click="agree_friend_request(value)"></el-button>
                                                <el-button type="danger" @click="refuse_friend_request(value)"></el-button>
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
                            <el-button type="info" size="medium" @click="send_remind">Add</el-button>
                        </div>
                        </template>
                        <div>
                            <el-input v-model="to_remind" placeholder="Things to remind" />
                        </div>
                        <div v-for="i in reminder">
                            <el-card class="box-card2">
                                <span>{{ i }}</span>
                                <div id="button-on-right">
                                    <el-button type="success" size="small" @click="del_remind(i)">Done</el-button>
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