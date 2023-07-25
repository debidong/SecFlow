<script>
import { ref } from 'vue'
import axios from 'axios'


export default {
    data() {
        return {
            myUid: '',
            myUsername: '',
            uid: '',
            username: '',
            rid: '',
            secretKey: '',
            isChecked: false,
            websocket: null
        }
    },
    methods: {
        // checkSKey() {
        //     params = {
        //         'secretKey': this.secretKey
        //     }
        //     axios.post('api/chat/check', data=params).then(
        //         response => {
        //             if(response.data['status'] == 'true') {
        //                 this.isChecked = true;
        //             }
        //         }
        //     )
        // }
        initialize() {
            this.myUid = this.$store.state.myUid;
            this.myUsername = this.$store.state.myUsername;
            this.uid = this.$store.state.uid;
            this.username = this.$store.state.username;
            this.rid=this.$store.state.rid;
        },
        connWS() {
            if(this.websocket == null) {
                this.websocket = new WebSocket('ws://localhost:8000/api/chat')
                this.$message('Joined in chatroom!')
            } else {
                this.$message('Already in chatroom!');
            }
        },
        disconnWS() {
            if(this.websocket == null) {
                this.$message('Already disconnected from chatroom!');
            }
            this.websocket.close();
            this.websocket = null;
            this.$message('Disconnected from chatroom!');
        },

        delRoom() {
            let url = 'api/chat/chatroom/' + this.rid;
            let config = {
                headers: {
                    'token': localStorage.getItem('token'),
                }
            }
            axios.delete(url, config=config).then((Response) => {
                this.disconnWS();
                this.$message('Chatroom deleted with chat history!');
            }).catch((error) => {
                this.$message('Chatroom already been deleted!');
            })
        }
    }, mounted() {
        this.initialize();
        this.connWS();
    }
}

</script>

<template>
    <el-container>
        <el-header>
            Chatroom
        </el-header>
        <el-container>
            <el-aside>
                You are chatting with {{ this.username }}
                <el-button type="warning" @click="disconnWS">Close Connection</el-button>
                <el-button type="success" @click="connWS">Connect</el-button>
                <el-button type="danger" @click="delRoom">Delete Chatroom</el-button>
            </el-aside>
            <el-main>
                
            </el-main>
        </el-container>
    </el-container>
</template>