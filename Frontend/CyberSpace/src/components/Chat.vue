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
            websocket: null,
            msg: '',
            chatHistory: []
        }
    },
    methods: {
        async keyExchange() {
          let dhParams = await window.crypto.subtle.generateKey({
            'name': 'EDCH',
            'namedCurve': 'P-256'
          })
          true,
          ['deriveKey']
        },
        initialize() {
            this.myUid = this.$store.state.myUid;
            this.myUsername = this.$store.state.myUsername;
            this.uid = this.$store.state.uid;
            this.username = this.$store.state.username;
            this.rid=this.$store.state.rid;
        },
        handleMsg() {
            let isFirstCall = true;

            const saveToLocal = (msg) => {
                if (isFirstCall) {
                    msg.forEach(params => {
                        this.chatHistory.push({
                            'sender': params.uid,
                            'time': params.time,
                            'content': params.content
                        })
                    })
                    isFirstCall = false;
                } else {
                    this.chatHistory.push({
                    'sender': msg.uid,
                    'time': msg.time,
                    'content': msg.content
                    })
                }
                
            }
            return saveToLocal
        },
        connWS() {
            if(this.websocket == null) {
                this.websocket = new WebSocket('ws://localhost:8000/api/chat/?rid=' + this.rid)
                this.$message('Joined in chatroom ' + this.rid + '!')
            } else {
                this.$message('Already in chatroom!');
            }
            let handleMsg = this.handleMsg()
            this.websocket.addEventListener('message', (event) => {
                let msg = JSON.parse(event.data) // typeof(msg) = string
                handleMsg(msg)
            })
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
        },

        sendMsg() {
            let params = {
                'myUid': this.myUid,
                'time': Date.now(),
                'content': this.msg,
                'rid': this.rid
            };

            this.websocket.send(JSON.stringify(params))
            this.msg = '';
        }
    }, mounted() {
        this.initialize();
        this.connWS();
    }, beforeUnmount() {
        this.websocket.close()
    }
}

</script>

<template>
    <el-container>
        <el-header class="el-header">
            <h1>
                Chatroom
            </h1>
            <el-breadcrumb :separator-icon="ArrowRight">
            <el-breadcrumb-item :to="{ path: '/' }">Home</el-breadcrumb-item>
            <el-breadcrumb-item :to="{ path: '/dashboard' }">Dashboard</el-breadcrumb-item>
            <el-breadcrumb-item :to="{ path: '/chat' }">Chat</el-breadcrumb-item>
            </el-breadcrumb>
        </el-header>
        <el-container>
            <el-main>
                <!-- message box -->
                <div>
                    <el-card>
                    <el-scrollbar height="500px">
                        <div v-for="(msg, index) in chatHistory" :key="index">
                            <el-divider content-position="left">{{ msg.sender }} @ {{ msg.time }}</el-divider>
                            <span>{{ msg.content }}</span>
                        </div>
                    </el-scrollbar>
                    </el-card>
                </div>
            </el-main>
            <el-aside>
                <div class="aside">
                    <el-card>
                        <template #header>
                            {{ this.username }}<br>
                            <el-text tag="i" type="success">Chatroom {{ this.rid }}</el-text>
                        </template>
                        <el-button type="warning" size="large" @click="disconnWS" id="button">Close Connection</el-button><br>
                        <el-button type="success" size="large" @click="connWS" id="button">Reconnect</el-button><br>
                        <el-button type="danger" size="large" @click="delRoom" id="button">Delete Chatroom</el-button><br>
                    </el-card>
                    <el-card>
                        <div class="inside-card">
                            <el-input
                            type="textarea"
                            :rows="3"
                            v-model="msg"
                            @keyup.enter.native="sendMsg"
                            placeholder=""/>
                        </div>
                        <div >
                            <el-button type="info" @click="sendMsg" id="button" size="default">Send</el-button>
                        </div>
                    </el-card>
                    
                </div>
            </el-aside>
        </el-container>
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

.aside {
    margin-left: 5%;
    text-align: center;
    font-size: large;
}

#button {
    width: 100%;
    margin: auto;
    margin-bottom: 1%;
}

.inside-card {
    margin-bottom: 5%;
}

</style>