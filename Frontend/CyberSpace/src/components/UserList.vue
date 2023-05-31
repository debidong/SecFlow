<script>
import axios from 'axios';

export default {
    data() {
        return {
            loaded: false,
            // myUid: '',
            // myUsername: '',
            // mySig: '',
            // isLogin: false,
            users: []
        }
    },
    mounted() {
        if(!this.loaded) {
            this.get_users();
        }
    },
    methods: {
        get_users() {
            axios.get('login/userList').then(
                response => {
                    this.users = response.data;
                }
            )
            this.loaded = true;
        },
        list_users() {
            
        }
    }
}
</script>

<template>
    <h1>UserList</h1>
    <table v-for="user in users">
        <tr>
            <td>Username</td>
            <td>Uid</td>
        </tr>
        <tr>
            <td>{{user['username']}}</td>
            <td>{{user['uid']}}</td>
        </tr>
    </table>
</template>