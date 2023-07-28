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
        }
    },
    methods: {
        submit() {
            if(this.uid == '' || this.password == '') {
                this.$message('Uid or password cannot be blank!')
                return;
            }
            let params = {
                'uid': this.uid,
                'username':this.username,
                'password':md5(this.password)
            };
            let config = {
                headers: {
                    'token': localStorage.getItem('token')
                }
            };

            axios.post('api/accounts/', params, config)
                .then(response => {
                        localStorage.setItem('token', response.headers['token']);
                        this.redirect_to_dashboard();
                    }).catch(error => {
                        this.$message("Uid or password isn't right!")
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
            <el-row>
                <el-col :span="8" />
                <el-col :span="8">
                    <el-card id="column" class="box-card">
                        <template #header>
                        <div class="card-header">
                            <span>Welcome back,<br>
                                <div id="welcome">
                                    {{ username }}
                                </div>
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
                            <el-button id="to_register" type="info" size="large" @click="$router.push({path: '/register'})">
                                Don't Have Accounts Yet?
                            </el-button>
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

.el-card {
    width: 50%;
}

#column {
    width: 100%;
}

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

#welcome {
    font-style: italic;
}
</style>