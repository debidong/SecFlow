<script>
import axios from 'axios';

export default {
    data() {
        return {
            uid: '',
            username: '',
            data: {},
            loaded: false
        }
    },
    methods: {
        require_get(params) {
            token = localStorage.getItem('token');
            var config = {
                headers: {
                    'token': token,
                }
            };
            axios.get('basic/', params, config)
            .then(response => {
                localStorage.setItem('token', response.response.headers['token']);
                this.data = response.data;
            })
        },
        get_user_info() {
            this.require_get({});
            this.uid = this.data['uid'];
            this.username = this.data['uid'];
        }
    },
    mounted() {
        this.get_user_info();
    }
}
</script>


<template>
    hi {{ uid }}
</template>