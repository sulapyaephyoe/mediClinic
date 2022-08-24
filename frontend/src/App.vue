<template>
  <div>
    <Navbar />
    
    <section class="section">
      <router-view/>
    </section>

    <Footer />
  
  </div>
</template>

<script>
import Navbar from '@/components/NavbarComponent';
import Footer from '@/components/FooterComponent.vue';

export default {
  name: 'App',
  components: {
    Navbar,
    Footer,
  }
}
</script>

<style>
body {
  margin: 0;
  padding: 0;
  background-color: #ffffff !important;
}

</style>
