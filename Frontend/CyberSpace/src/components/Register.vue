<script>
import axios from 'axios'
import md5 from 'js-md5'

export default {
    data() {
        return {
            uid: '1',
            username: '1',
            password: '1',
            isRegistered: false,
        }
    },
    methods: {
        register() {
            var params = {
                'uid': this.uid,
                'username':this.username,
                'password':md5(this.password)
            };
            axios.post('api/accounts/register', params).then(
                response => {
                        this.isRegistered = true;
                }
            ).catch(error => {
                this.$message('Uid is occupied. Choose another uid.')
            })
        }
    }
}
</script>


<template>
    <el-container>
        <el-header>
                <h1>
                    Registration
                </h1>
        </el-header>
            <el-main>
                <el-row>
                    <el-col :span="8" />
                    <el-col :span="8">
                        <div v-if="isRegistered == false">
                            <el-card class="box-card">
                                <template #header>
                                    <div class="card-header">
                                        Thank you for registering,<br>
                                        <div id="welcome">
                                            {{ username }}
                                        </div>
                                    </div>
                                </template>
                                <el-input v-model="uid" placeholder="Uid" />
                                <el-input v-model="username" placeholder="Username" />
                                <el-input v-model="password" placeholder="Password" />
                                <div id="submit">
                                    <el-button id="button" type="success" size="large" @click="register">Submit</el-button>
                                </div>
                            </el-card>
                        </div>

                        <!-- Registration succeeded -->
                        <div v-else-if="isRegistered == true">
                            <el-card>
                                <template #header>
                                    <div class="card-header1">
                                        <span>You are in!</span>
                                        <el-button id="to_login" size="default" text @click="$router.push({path: '/login'})">
                                        Login
                                        </el-button>
                                    </div>
                                </template>
                                <div>
                                    Your uid: {{ uid }}
                                <br>
                                    Your username: {{ username }}
                                <br>
                                    Keep that in mind.
                                </div>
                            </el-card>

                        </div>
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

#submit {
    margin-top: 5%;
}

#button {
    width: 100%;
    margin: auto;
}

#welcome {
    font-style: italic;
}
</style>