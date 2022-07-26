<template>
  <div>
    <Navbar />
    
    <section class="section">
      <router-view/>
    </section>
  
  </div>
</template>

<script>
import Navbar from '@/components/NavbarComponent';

export default {
  name: 'App',
  components: {
    Navbar,
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
