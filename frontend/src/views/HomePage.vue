<template>

<div id="carouselExampleIndicators" class="carousel slide img-height" data-ride="carousel" style="width:90%; height:600px !important;">
    <ol class="carousel-indicators">
        <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
        <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
        <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
    </ol>
    <div class="carousel-inner">
        <div class="carousel-item active">
            <img class="d-block w-80 img-height" src="@/assets/images/slideImg1.jpg" alt="First slide">
            <!-- <div class="carousel-caption d-none d-md-block">
                <h5>My Caption Title (1st Image)</h5>
                <p>The whole caption will only show up if the screen is at least medium size.</p>
            </div> -->
        </div>
        <div class="carousel-item">
            <img class="d-block w-80 img-height" src="@/assets/images/slideImg2.jpg" alt="Second slide">
        </div>
        <div class="carousel-item">
            <img class="d-block w-80 img-height" src="@/assets/images/slideImg3.jpg" alt="Third slide">
        </div>
    </div>
    <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true" style="color:green"></span>
        <span class="sr-only">Previous</span>
    </a>
    <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true" style="color:green"></span>
        <span class="sr-only">Next</span>
    </a>
</div>

  <div class="container marketing">

    <!-- Three columns of text below the carousel -->
    <div class="row circlepattern">
      <div class="col-lg-4">
        <img class="bd-placeholder-img rounded-circle" width="140" height="140" src="@/assets/images/hospital1.jpg" />

        <h2>Victoria</h2>
        <p>Your healthy life is our mission. You can enquery us about our services and packages.</p>
        <p><router-link to='/hospitals/view-hospital'  class="btn btn-secondary" @click="setHID(3)">View details &raquo;</router-link></p>
      </div><!-- /.col-lg-4 -->
      <div class="col-lg-4">
        <img class="bd-placeholder-img rounded-circle" width="140" height="140" src="@/assets/images/hospital2.jpg" />

        <h2>Grand Hantha</h2>
        <p>Your healthy life is our mission. You can enquery us about our services and packages.</p>
        <p><router-link to='/hospitals/view-hospital'  class="btn btn-secondary" @click="setHID(3)">View details &raquo;</router-link></p>


      </div><!-- /.col-lg-4 -->
      <div class="col-lg-4">
        <img class="bd-placeholder-img rounded-circle" width="140" height="140" src="@/assets/images/hospital3.jpg" />

        <h2>Bahosi</h2>
        <p>Your healthy life is our mission. You can enquery us about our services and packages.</p>
        <p><router-link to='/hospitals/view-hospital'  class="btn btn-secondary" @click="setHID(2)">View details &raquo;</router-link></p>
      </div><!-- /.col-lg-4 -->
    </div><!-- /.row -->


    <!-- START THE FEATURETTES -->

    <hr class="featurette-divider">
    <div>
       <section id="contact">
  
  <h1 class="section-header">Contact us</h1>
  
  <div class="contact-wrapper">
  
  <!-- Left contact page --> 
    
    <form id="contact-form" class="form-horizontal" role="form">
       
      <div class="form-group">
        <div class="col-sm-12">
          <input type="text" class="form-control" id="name" placeholder="NAME" name="name" value="" required>
        </div>
      </div>

      <div class="form-group">
        <div class="col-12">
          <input type="email" class="form-control" id="email" placeholder="EMAIL" name="email" value="" required>
        </div>
      </div>
      <div class="form-group">
        <div class="col-12">
          <textarea class="form-control" rows="10" placeholder="MESSAGE" name="message" required></textarea>
        </div>
      </div>
        <button class="btn btn-primary send-button" id="submit" type="submit" value="SEND"> SEND
        </button>
    </form>
    
  <!-- Left contact page --> 
    
      <div class="direct-contact-container">

        <ul class="contact-list">
          <li class="list-item"><i class="bi bi-geo-alt"><span class="contact-text place">Yangon,</span></i></li>
          
          <li class="list-item"><i class="bi bi-telephone"><span class="contact-text phone"><a href="tel:1-212-555-5555" title="Give me a call">(95) 09-796762086</a></span></i></li>
          
          <li class="list-item"><i class="bi bi-envelope-open"><span class="contact-text gmail"><a href="mailto:#" title="Send me an email">admin@gmail.com</a></span></i></li>
          
        </ul>


      </div>
    
  </div>
  
</section>  
  
    </div>
</div>
</template>
    

<script>

export default {
    name:'HomePage',
    methods: {
        setHID(hid) {
            localStorage.setItem('hid',hid)
        }
    }
}
</script>

<style>
.img-height {
  width: 90% !important;
  height: 600px !important;
  margin: 0 auto;
}
.carousel-control-next-icon {
   background-image: url(https://cdn-icons-png.flaticon.com/512/130/130884.png) !important;
}
.carousel-control-prev-icon {
   background-image: url(https://cdn-icons-png.flaticon.com/512/130/130882.png) !important;
}
.pattern {
    width: 80% !important;
    height: 600px !important;
    margin: 0px 150px 0px 150px !important; 
    align-items: center;
    justify-content: center !important;
    
}

.circlepattern {
    width: 80% !important;
    height: 400px !important;
    margin: 0px 150px 0px 150px !important; 
    align-items: center;
    justify-content: center !important;
}
#contact {
  width: 100%;
  height: 100%;
  background-color: #3c414b;
}

.section-header {
  text-align: center;
  margin: 0 auto;
  padding: 40px 0;
  font: 300 60px 'Oswald', sans-serif;
  color: #fff;
  text-transform: uppercase;
  letter-spacing: 6px;
}

.contact-wrapper {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin: 0 auto;
  padding: 20px;
  position: relative;
  max-width: 840px;
}

/* Left contact page */
.form-horizontal {
  /*float: left;*/
  max-width: 400px;
  font-family: 'Lato';
  font-weight: 400;
}

.form-control, 
textarea {
  width: 400px !important;
  background-color: #000;
  color: #fff;
  letter-spacing: 1px;
}


/* Begin Right Contact Page */
.direct-contact-container {
  max-width: 400px;
}

/* Location, Phone, Email Section */
.contact-list {
  list-style-type: none;
  margin-left: -30px;
  padding-right: 20px;
}

.list-item {
  line-height: 4;
  color: #aaa;
}

.contact-text {
  font: 300 18px 'Lato', sans-serif;
  letter-spacing: 1.9px;
  color: #bbb;
}

.send-button {
    width:100px;
    height: 50px;
    margin: 0px 0px 0px 150px !important;
}
.place {
  margin-left: 62px;
}

.phone {
  margin-left: 56px;
}

.gmail {
  margin-left: 53px;
}

.contact-text a {
  color: #bbb;
  text-decoration: none;
  transition-duration: 0.2s;
}

.contact-text a:hover {
  color: #fff;
  text-decoration: none;
}


hr {
  border-color: rgba(255,255,255,.6);
}

</style>