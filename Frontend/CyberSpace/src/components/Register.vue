<script>
import axios from 'axios'
import md5 from 'js-md5'
// axios.defaults.baseURL = 'http://0.0.0.0:8000'

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
    <div v-if="status == 'false'">
        <h1>Registration</h1>
        <br>
        <input v-model="uid">Uid
        <br>
        <input v-model="username">Username
        <br>
        <input v-model="password">Password
        <br>
        <span v-if="is_occupied=='true'">Uid occupied!</span>
        <button @click="register">Submit</button>
    </div>
    <div v-else-if="status == 'true'">
        {{ status }}
        <h1>Registration succeeded.</h1>
        Your uid: {{ uid }}
        <br>
        Your username: {{ username }}
        <br>
        Your password: {{ password }}
        <br>
        Keep that in mind.
        <router-link to="/login">Login</router-link>
    </div>


</template>