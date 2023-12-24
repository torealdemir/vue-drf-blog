<template>
    <nav class="navbar navbar-expand-md bg-success">
        <a href="" class="navbar-brand fs-3 ms-3 text-secondary ">ToBlog</a>
        <a href="#" class="nav-link mx-3 fs-4">News</a>
        <a href="#" class="nav-link mx-3 fs-4">About</a>
        

        <button class="navbar-toggler text-warning m-3" type="button" data-bs-toggle="collapse" data-bs-target="#btn"  ><i class="bi bi-body-text">T</i></button>
        <div class="collapse navbar-collapse" id="btn">
            <ul class="navbar-nav ms-auto">
            <li class="nav-item">
                <router-link to="login/" class="btn btn-warning mx-4">login</router-link>
            </li>
            <li class="nav-item">
                <router-link to="sign-up/" class="btn btn-primary mx-3">SignUp</router-link>
            </li>
            </ul>
        </div>

</nav>

</template>