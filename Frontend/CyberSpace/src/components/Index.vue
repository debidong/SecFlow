<template>
    <h1>Welcome to <text id="cyberspace">CyberSpace</text>!</h1>
    <br>
    <div id="instructions">
        <h2>What for?</h2>
        <p>CyberSpace is a chatroom with end-to-end encryption technologies,
            which tries to ensure your privacy in conversations. Server-side
            will not save your chat history, while you are able to save your
            chat history in browser-side.
        </p>
        <h2>How?</h2>
        <p>The app uses the AES/RSC suite to secure the safety during transportation, which is designed carefully to make sure either safety
            or speed is ensured when using this app. 
        </p>
    </div>

    <div>
        <router-link to="/login">Login</router-link>
        <router-link to="/userList">User List</router-link>
    </div>
</template>