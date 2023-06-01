<script>
// element UI setting
import { ref } from 'vue'
import md5 from 'js-md5'

const input = ref('')
import {
  Check,
  Delete,
  Edit,
  Message,
  Search,
  Star,
} from '@element-plus/icons-vue'

import axios from 'axios'
axios.defaults.baseURL = 'http://127.0.0.1:8000'

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

            axios.post('login/', params, config)
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
    <div class="page">
        <el-card class="box-card">
        <template #header>
        <div class="card-header">
            <span>Welcome: {{ uid }}</span>
            <el-button @click="submit">Login</el-button>
        </div>
        </template>
        <el-input v-model="uid" placeholder="Uid" />
        <el-input
        v-model="password"
        placeholder="Password"
        show-password/>
        <el-link v-if="!is_null" type="primary" href="./login/register">Don't have accounts yet?</el-link>
        <el-text v-if="is_null" type="warning">Uid or password cannot be empty.</el-text>
        </el-card>
    </div>
</template>

<style scoped>
.el-link {
  margin-right: 8px;
}
.el-link .el-icon--right.el-icon {
  vertical-align: text-bottom;
}

card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}

.box-card {
    /* width: 480px; */
    /* width: 50%;
    height: 50%; */
    position: absolute;
}

.page {
    position: relative;
}
</style>