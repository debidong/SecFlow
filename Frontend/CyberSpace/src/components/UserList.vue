<script>
import axios from 'axios';


export default {
    data() {
        return {
            loaded: false,
            users: [],
            found: false,
            uid_to_find: ''
        }
    },
    mounted() {
        if(!this.loaded) {
            this.get_users();
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
        get_users() {
            this.require_get('userList').then((data) => {
                this.users = data['user'];
            })
            this.loaded = true;
        },
        find_user_by_id() {
            var param = {
                'uid': this.uid_to_find
            };

            this.require_post('userList', param).then((data) => {
                this.users = data['user'];
                this.found = true;
            }).catch(error => {
                    this.users = [];
                    this.found = false;
                    this.user_not_exist();
                }
            );
        },
        user_not_exist() {
            this.$message('User not exists!');
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
            </div>
            </template>
            <div>
                <el-input id="search-input" v-model="uid_to_find" placeholder="User" />
                <el-button id="search" type="success" size="large" @click="find_user_by_id">Search</el-button>
            </div>
        </el-card>

        <el-card class="box-card" v-if="found">
            <template #header>
            <div class="card-header">
                <span>Result</span>
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
    width: 20%;
    margin: auto;
}

/* #search-input {
    width: 80%;
} */
</style>