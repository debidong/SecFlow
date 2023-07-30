<script>
import axios from 'axios'
import md5 from 'js-md5'

export default {
    data() {
        return {
            uid: '',
            username: '',
            password: '',
            email: '',
            code: '',
            isRegistered: false,
        }
    },
    methods: {
      sendCode() {
        if (this.email != '') {
          let params = {
            'email': this.email,
          }
          axios.post('api/accounts/register/code', params).then(response => {
            let status = response.data['status']
            if (status == 'true') {
              this.$message('An email for verification has been sent.')
            }
          }).catch(error => {
            this.$message('Error.')
          })
        } else {
          this.$message('Please enter your email first.')
        }
        
      },
      register() {
          let params = {
              'uid': this.uid,
              'username':this.username,
              'password':md5(this.password),
              'email': this.email,
              'code': this.code
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
                            <el-row>
                              <el-col :span="4">
                                <div class="option">
                                  Uid
                                </div>
                              </el-col>
                              <el-col :span="20">
                                  <el-input v-model="uid" placeholder="CANNOT be modified after registration" />
                              </el-col>
                            </el-row>
                            <el-row>
                              <el-col :span="4">
                                <div class="option">
                                  Username
                                </div>
                              </el-col>
                              <el-col :span="20">
                                <el-input v-model="username" placeholder="A cool name others call you by" />
                              </el-col>
                            </el-row>
                            <el-row>
                              <el-col :span="4">
                                <div class="option">
                                  Password
                                </div>
                              </el-col>
                              <el-col :span="20" class="option">
                                <el-input v-model="password" placeholder="Make it uneasy to guess" />
                              </el-col>
                            </el-row>
                            <el-row>
                              <el-col :span="4">
                                <div class="option">
                                  Email
                                </div>
                              </el-col>
                              <el-col :span="20">
                                <el-input v-model="email" placeholder="Only one account for one email">
                                  <template #append>
                                    <el-button @click="sendCode">Send code</el-button>
                                  </template>
                                </el-input>
                              </el-col>
                            </el-row>
                            <el-row>
                              <el-col :span="4">
                                <div class="option">
                                  Code
                                </div>
                              </el-col>
                              <el-col :span="20">
                                <el-input v-model="code" placeholder="Check your email after clicking the button" />
                              </el-col>
                            </el-row>
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

.option {
  font-size: x-small;
  justify-content: center;
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