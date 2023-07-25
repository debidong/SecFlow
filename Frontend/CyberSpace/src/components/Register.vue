<script>
import axios from 'axios'
import md5 from 'js-md5'

export default {
    data() {
        return {
            uid: '',
            username: '',
            password: '',
            status: 'false',
            is_occupied: 'false'
        }
    },
    methods: {
        register() {
            var reg = {
                'uid': this.uid,
                'username':this.username,
                'password':md5(this.password)
            };
            axios.post('api/accounts/register', reg).then(
                response => {
                    if(response.data['status'] == 'occupied') {
                        this.is_occupied = 'true';
                    }
                    if(response.data['status'] == 'true') {
                        this.is_occupied = 'false';
                        this.status = 'true';
                    }

                }
            )
        }
    }
}
</script>


<template>
    <el-container>
        <div v-if="status == 'false'">
            <el-header>
                <h1>
                    Registration
                </h1>
            </el-header>
            <el-main>
                <el-card class="box-card">
                    <template #header>
                        <div class="card-header">
                        <span>Welcome,<br>
                        {{ uid }}
                        </span>
                        </div>
                    </template>
                    <el-input v-model="uid" placeholder="Uid" />
                    <el-input v-model="username" placeholder="Username" />
                    <el-input v-model="password" placeholder="Password" />
                    <span v-if="is_occupied=='true'">Uid occupied!</span>
                    <el-button id="login" type="success" size="large" @click="register">Submit</el-button>
                </el-card>
            </el-main>
        </div>

        <div v-else-if="status == 'true'">
            <el-card>
                <template #header>
                    Registration succeeded.
                </template>
                <div>
                    Your uid: {{ uid }}
                <br>
                    Your username: {{ username }}
                <br>
                    Keep that in mind.
                </div>
            </el-card>
            <el-button id="to_login" type="success" size="large" @click="$router.push({path: '/login'})">
                    Login
            </el-button>
        </div>
    </el-container>
</template>

<style scoped>



</style>