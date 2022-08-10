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
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            Hospitals
          </a>
          <div class="dropdown-menu" aria-labelledby="navbarDropdown">
            <router-link to="/hospitals/add-hospital" class="nav-link">Add Hospital</router-link>
            <div class="dropdown-divider"></div>
            <router-link to="/hospitals/view-hospital" class="nav-link">View Hospitals</router-link>
          </div>
        </li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          Doctors
        </a>
        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
          <router-link to="/doctors/doctorslist" class="nav-link">Doctors' List</router-link>
          <div class="dropdown-divider"></div>
          <router-link to="" class="nav-link">Schedule</router-link>
        </div>
      </li>
        <li class="nav-item px-3 me-2">
          <a class="nav-link" href="#">Shops</a>
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