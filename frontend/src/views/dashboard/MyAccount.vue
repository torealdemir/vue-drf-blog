<template>
    <div class="about">
        <h1>MyAcoount</h1>

        <button class="btn btn-danger" @click="logout()">Logout</button>
    </div>
  </template>

<script>
export default {
    methods: {
        logout(){
            console.log('Logout')
        }
    }
}

</script>
  