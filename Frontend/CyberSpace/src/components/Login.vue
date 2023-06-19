<script>
// element UI setting
import { ref } from 'vue'
import md5 from 'js-md5'

const input = ref('')

import axios from 'axios'

export default {
    data() {
        return {
            uid: '',
            password: '',
            is_null: false,
        }
    },
    methods: {
        submit() {
            if(this.uid == '' || this.password == '') {
                this.is_null = true;
                return;
            }
            var params = {
                'uid': this.uid,
                'username':this.username,
                'password':md5(this.password)
            };
            var config = {
                headers: {
                    'token': localStorage.getItem('token')
                }
            };

            axios.post('api/accounts/', params, config)
                .then(response => {
                    if(response.data['status'] == 'true') {
                        localStorage.setItem('token', response.headers['token']);
                        this.redirect_to_dashboard();
                    }

            }).catch(error => {
                console.log(error)
            })
        },
        redirect_to_dashboard() {
            this.$router.push({path: '/dashboard', replace: 'true'});
        }
    }
};
</script>

<template>
    <el-container>
        <el-header>
            <h1>
                Login
            </h1>
        </el-header>
        <el-main>
            <el-card class="box-card">
                <template #header>
                <div class="card-header">
                    <span>Welcome back,<br>
                        {{ uid }}
                    </span>
                </div>
                </template>
                <el-input v-model="uid" placeholder="Uid" />
                <el-input
                v-model="password"
                placeholder="Password"
                show-password/>
                <div id="submit">
                    <el-button id="login" type="success" size="large" @click="submit">Login</el-button>
                    <el-button id="to_register" type="info" size="large" @click="$router.push({path: '/login/register'})">
                        Don't Have Accounts Yet?
                    </el-button>
                </div>
                <el-text v-if="is_null" type="warning">Uid or password cannot be empty.</el-text>
            </el-card>
        </el-main>
    </el-container>
    
</template>

<style scoped>
/* .el-button {
    margin: auto;
} */
#submit {
    margin-top: 5%;
}

#to_register {
    width: 49%;
    margin: auto;
    margin-left: 1%;
}

#login {
    width: 49%;
    margin: auto;
    margin-right: 1%;
}
</style>