<template>
  <div class="container-fluid" style="padding-right: 0px;  padding-left: 0px;">
    <!--header top-->
    <div class="header-top">
      <div class="container clearfix">
        <div class="top-left">
          <h6>Opening Hours : Saturday to Sunday - 24 Hours</h6>
        </div>
        <div class="top-right">
          <ul class="social-links">
            <li>
              <a class="btn btn-outline-light btn-floating m-1" href="https://www.facebook.com/lapyae.phyoe.58/">
                <i class="bi bi-facebook"></i>
              </a>
            </li>
            <li>
              <a class="btn btn-outline-light btn-floating m-1" href="#!" role="button"><i
                class="bi bi-twitter"></i>
              </a>

            </li>
            <li>
              <!-- Instagram -->
              <a class="btn btn-outline-light btn-floating m-1" href="#!" role="button"><i
                  class="bi bi-instagram"></i></a>
            </li>
            <li>
              <!-- Linkedin -->
              <a class="btn btn-outline-light btn-floating m-1" href="#!" role="button"><i
                  class="bi bi-linkedin"></i></a>
            </li>
            <li>
              <!-- Github -->
              <a class="btn btn-outline-light btn-floating m-1" href="https://github.com/sulapyaephyoe/mediClinic.git"
                role="button"><i class="bi bi-github"></i></a>
            </li>
          </ul>
        </div>
      </div>
    </div>
    <!--header top-->
    <!--Header Upper-->
    <section class="header-uper">
      <div class="container clearfix">
        <div class="logo">
          <figure>
            <img src="@/assets/icon2.jpg" class="logo-icon" />
            <span class="logo-text">MediClinic</span>
          </figure>
        </div>
        <div class="right-side">
          <ul class="contact-info">
            <li class="item">
              <div class="icon-box">
                <i class="bi bi-envelope"></i>
              </div>
              <strong>Email</strong>
              <br>
              <a href="mailto:#" title="Send me an email">
                <span id="text-color">admin@gmail.com</span>
              </a>
            </li>
            <li class="item">
              <div class="icon-box">
                <i class="bi bi-telephone-fill"></i>
              </div>
              <strong>Call Now</strong>
              <br>
              <a href="tel:1-212-555-5555" title="Give me a call">
                <span id="text-color">(95) 09-796762086</span>
              </a>
            </li>
          </ul>
          <div class="link-btn">
            <router-link to="/booking" class="btn-style-one">Consulting</router-link>
          </div>
        </div>
      </div>
    </section>
    <!--Header Upper-->
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-light">
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
         <!-- Left links -->
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <router-link to="/" class="nav-link" id="hpnavbar">Home</router-link>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown"
                aria-haspopup="true" aria-expanded="false" style="color: #fff;font-size: 15px;">
                Hospitals
              </a>
              <div class="dropdown-menu" aria-labelledby="navbarDropdown" id="dropdownmenu">
                <router-link to="/hospitals/add-hospital" class="nav-link" id="nav-link" style="padding:12px 18px 12px 22px;" v-if="$store.state.isAdmin">Add Hospital</router-link>
                <router-link to="/hospitals/view-hospital" class="nav-link" id="nav-link">View Hospitals</router-link>
                <router-link to="/hospitals/schedule_list" class="nav-link" id="nav-link">Schedules</router-link>
              </div>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown"
                aria-haspopup="true" aria-expanded="false" style="color: #fff;font-size: 15px;">
                Doctors
              </a>
              <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                <router-link to="/doctorslist" class="nav-link" id="nav-link" v-if="$store.state.isAdmin">Doctors' List</router-link>
                <router-link to="/schedule_list" class="nav-link" id="nav-link">Schedules</router-link>
              </div>
            </li>
            <li class="nav-item px-3 me-2">
              <router-link to="/timetable" class="nav-link" href="#" id="hpnavbar">Timetable (Specialist)</router-link>
            </li>
          </ul>
          <ul class="navbar-nav topnav-right">
            <router-link to="/login" class="nav-link" style="color:#fff" v-if="!$store.state.isAuthenticated">LOG IN</router-link>
            <a class="nav-link" style="color:#fff" @click="logout()" v-if="$store.state.isAuthenticated">LOG OUT</a>
          </ul>
      </div>
    </nav>
    <!-- Navbar -->
  </div>
</template>

<script>
export default {
  name: 'NavbarComponent',
  methods: {
    logout() {
      this.$store.commit('adminRole', false)
      this.$store.commit('removeToken')
      this.$router.push('/')
    }
  }
}
</script>

<style scoped>
.logo-icon {
  width: 40px;
  height: 40px;
  margin-top: -26px;
}
.logo-text {
  font-family: monospace;
  font-size: 30px;
  margin-left: 30px;
  color: #615f5f;
  font-weight: bold;
}

.topnav-right {
  float: right;
  margin-right: 100px;
}

#nav-link:hover {
  background-color: #eee;
}

#nav-link {
  padding: 12px 18px 12px 22px;
  text-transform: none;
}
#navbarSupportedContent{
  margin-left: 200px;
}
.navbar-toggler{
  margin:10px 10px 10px 10px;
}
</style>