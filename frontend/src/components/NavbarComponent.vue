<template>
<div>

    <!-- Navbar -->
<nav class="navbar navbar-expand-lg navbar-light">
  <!-- Container wrapper -->
  <div class="container">
    <!-- Navbar brand -->
    <img src="@/assets/icon1.png" class="logo-icon"/>
    <span class="logo-text">MediClinic</span>

    <!-- Collapsible wrapper -->
    <div class="collapse navbar-collapse" id="navbarButtonsExample">
      <!-- Left links -->
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Departments</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Doctors</a>
        </li>
        <li class="nav-item px-3 me-2">
          <a class="nav-link" href="#">Shops</a>
        </li>
        <li class="nav-item px-3 me-3">
            <a class="btn btn-dark px-3" href="https://github.com/mdbootstrap/mdb-ui-kit" role="button"><i class="fab fa-github"></i></a>
        </li>
      </ul>
    </div>
    <!-- Collapsible wrapper -->
  </div>
  <!-- Container wrapper -->
</nav>
<!-- Navbar -->
      

</div>
</template>

<script>
export default {
    name: 'NavbarComponent',
}
</script>

<style scoped>
.logo-icon {
    width: 40px;
    height: 40px;
    margin: 50px 10px 50px 100px;
}
.logo-text {
    font-family: monospace;
    font-size: 30px;
    margin: 50px 200px 50px 0px;
}

</style>