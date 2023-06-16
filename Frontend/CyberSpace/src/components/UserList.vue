<script>
import axios from 'axios';
axios.defaults.baseURL = 'http://127.0.0.1:8000'

export default {
    data() {
        return {
            loaded: false,
            users: [], // returned userList
            found: false, // if the user is founded
            uid_to_find: ''

        }
    },
    // mounted() {
    //     if(!this.loaded) {
    //         this.get_users();
    //     }
    // },
    methods: {
        // template for HTTP get
        // Requested URL: user/dashboard/ + INPUT
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

        // template for HTTP post
        // requested URL: user/dashboard/ + INPUT
        require_post(url, param) {
            var token = localStorage.getItem('token');
            var config = {
                headers: {
                    'token': token,
                }
            };
            var _url = 'user/dashboard/userList' + url;
            return axios.post(_url, param, config).then(
                (response) => response.data
            )

        },

        // // get all users in database
        // get_users() {
        //     this.require_get('userList').then((data) => {
        //         this.users = data['user'];
        //         this.me=data['me'];
        //     })
        //     this.loaded = true;
        // },

        // find a user by its id
        find_user_by_id() {
            var param = {
                'uid': this.uid_to_find
            };
            this.require_post('', param).then((data) => {
                this.users = data['user'];
                this.found = true;
                this.me = data['me'];
            }).catch(error => {
                    this.users = [];
                    this.found = false;
                    this.user_not_exist();
                }
            );
        },

        // alert when cannot find users
        user_not_exist() {
            this.$message('User not exists!');
        },

        // alert when a friend request is sent
        friend_request_sent(status) {
            if(status == 'true') {
                this.$message('Request sent!');
            } else if(status == 'already sent') {
                this.$message('Already sent request.')
            } else if(status == 'false') {
                this.$message('Something went wrong.')
            }
        },

        // send a friend request to a user
        send_friend_request() {
            var param = {
                'user': this.users['uid']
            }
            this.require_post('/friendRequest', param).then((data) => {
                this.friend_request_sent(data['status']);
            }).catch(error => {
                this.friend_request_sent(error.response.data['status']);
            })
        }       
    }
}
</script>

<template>
    <el-container>
        <el-header>
            <h1>UserList</h1>
        </el-header>
    </el-container>
    <el-main>
        <el-breadcrumb :separator-icon="ArrowRight">
            <el-breadcrumb-item :to="{ path: '/' }">Home</el-breadcrumb-item>
            <el-breadcrumb-item :to="{ path: '/dashboard' }">Dashboard</el-breadcrumb-item>
            <el-breadcrumb-item :to="{ path: '/dashboard/userList' }">UserList</el-breadcrumb-item>
        </el-breadcrumb>


        <el-card class="box-card">
            <template #header>
            <div class="card-header">
                <span>Search</span>
                <div>
                    <el-button id="search" type="info" size="large" @click="find_user_by_id">Search User</el-button>
                </div>
            </div>
            </template>
            <div>
                <el-input id="search-input" v-model="uid_to_find" placeholder="User" />
            </div>
            
        </el-card>

        <el-card class="box-card" v-if="found">
            <template #header>
            <div class="card-header">
                <span>Result</span>
                <div id="add-contact">
                    <el-button id="add-contact" type="success" size="large" @click="send_friend_request">Add friend</el-button>
                </div>
            </div>
            </template>
            <div>
                Uid: {{ users['uid'] }}
                Username: {{ users['username'] }}
            </div>
        </el-card>
    </el-main>
</template>

<style scoped>
.el-header {
    position: relative;
    text-align: center;
    justify-content: center;
    font-size: x-large;
    margin-bottom: 10%;
}
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: larger;
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

.box-card {
  font-size: large;
  margin-top: 3%;

}

#search {
    /* width: 20%; */
    margin: auto;
}
</style>