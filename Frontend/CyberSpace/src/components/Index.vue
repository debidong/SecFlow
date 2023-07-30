<script>
export default {
    data() {
        return{
            infos: {
                "What's this?": 'SecFlow is a chatroom with end-to-end encryption technologies,\n\
                which tries to ensure your privacy in conversations. Server-side\n\
                will not save your chat history, while you are able to save your\n\
                chat history in browser-side.',
                'How?': 'The app uses AES/RSC suite to secure the safety during transportation,\n\
                which is designed carefully to make sure either safety or speed is ensured when using this app.'
            }
        }
        
    }
}
</script>


<template>
<div class="common-layout">
    <el-container>
      <el-header><h1>SecFlow</h1></el-header>
      <el-main>
        <el-carousel :interval="5000" arrow="hover">
            <el-carousel-item v-for="(value, key) in infos">
                <el-card class="box-card">
                <template #header>
                <div class="card-header">
                    <span>{{ key }}</span>
                </div>
                </template>
                <div>
                    {{ value }}
                </div>
                </el-card>
        </el-carousel-item>
        </el-carousel>
            
            
      </el-main>
      <el-footer>
        <el-button type="success" size="large" @click="$router.push({path: '/login'})">Login</el-button>
        <el-button type="info" size="large" @click="$router.push({path: '/userlist'})">Find Out Users</el-button>    
      </el-footer>
    </el-container>
</div>
    
</template>

<style scoped>
.el-header {
    position: relative;
    text-align: center;
    justify-content: center;
    font-size: x-large;
    margin-bottom: 10%;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: larger;
  font-weight: bold;
}

/* .text {
  font-size: 17px;
} */

.item {
  margin-bottom: 18px;
}

.box-card {
  width: 60%;
  font-size: large;
  margin-top: 1%;
  margin-bottom: 1%;
  margin-left: auto;
  margin-right: auto;
}

.el-button {
    width: 20%;
}

.el-footer {
    margin-top: 1%;
    text-align: center;
}
</style>