<template>
    <!--footer-main-->
    <footer class="footer-main">
        <div class="footer-top">
            <div class="container">
                <div class="row">
                    <div class="col-md-6 col-sm-6 col-xs-12">
                        <div class="about-widget">
                            <div class="footer-logo">
                                <figure>
                                    <img src="@/assets/icon3.png" class="footerlogo-icon"/>
                                    <span class="logo-text">MediClinic</span>
                                </figure>
                            </div>
                            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestias, temporibus?</p>
                            <ul class="location-link">
                                <li class="item">
                                    <i class="bi bi-geo-alt-fill"></i>
                                    <p>Yangon,</p>
                                </li>
                                <li class="item">
                                    <i class="bi bi-envelope" aria-hidden="true"></i>
                                    <a href="mailto:#" title="Send me an email">
                                        <p>admin@gmail.com</p>
                                    </a>
                                </li>
                                <li class="item">
                                    <i class="bi bi-telephone-fill" aria-hidden="true"></i>
                                    <a href="tel:1-212-555-5555" title="Give me a call">
                                        <p>(95) 09-796762086</p>
                                    </a>
                                </li>
                            </ul>
                            <!-- Section: Social media -->
                            <section class="mb-4">
                                <!-- Facebook -->
                                <a class="btn btn-outline-light btn-floating m-1"
                                    href="https://www.facebook.com/lapyae.phyoe.58/" role="button"><i
                                        class="bi bi-facebook"></i></a>

                                <!-- Twitter -->
                                <a class="btn btn-outline-light btn-floating m-1" href="#!" role="button"><i
                                        class="bi bi-twitter"></i></a>

                                <!-- Google -->
                                <a class="btn btn-outline-light btn-floating m-1" href="#!" role="button"><i
                                        class="bi bi-google"></i></a>

                                <!-- Instagram -->
                                <a class="btn btn-outline-light btn-floating m-1" href="#!" role="button"><i
                                        class="bi bi-instagram"></i></a>

                                <!-- Linkedin -->
                                <a class="btn btn-outline-light btn-floating m-1" href="#!" role="button"><i
                                        class="bi bi-linkedin"></i></a>

                                <!-- Github -->
                                <a class="btn btn-outline-light btn-floating m-1" href="#!" role="button"><i
                                        class="bi bi-github"></i></a>
                            </section>
                            <!-- Section: Social media -->
                        </div>
                    </div>
                    <div class="col-md-6 col-sm-6 col-xs-12">
                        <h6 class="ml-3" style="font-size:larger">Contact us</h6>
                        <div>
                            <section id="contact">

                                <div class="contact-wrapper">

                                    <!-- Left contact page -->

                                    <form id="contact-form" class="form-horizontal" role="form">

                                        <div class="form-group">
                                            <div class="col-sm-12">
                                                <input type="text" class="form-control hpform" id="name" placeholder="NAME"
                                                    name="name" value="" required>
                                            </div>
                                        </div>

                                        <div class="form-group">
                                            <div class="col-12">
                                                <input type="email" class="form-control hpform" id="email" placeholder="EMAIL"
                                                    name="email" value="" style="margin-top: -16px;" required>
                                            </div>
                                        </div>
                                        <div class="form-group">
                                            <div class="col-12">
                                                <textarea class="form-control hpform" rows="10" placeholder="MESSAGE"
                                                    name="message" style="margin-top: -16px;" required></textarea>
                                            </div>
                                        </div>
                                        <button class="btn-style-one send-button ml-3 mt-3" id="submit" type="submit"
                                            value="SEND"> SEND
                                        </button>
                                    </form>
                                </div>

                            </section>

                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <div class="container clearfix">
                <div class="copyright-text">
                    <p>&copy;2022 Copyright: <a class="text-white"
                            href="https://github.com/sulapyaephyoe/mediClinic.git">Mediclinic.com</a>
                    </p>
                </div>
            </div>
        </div>
    </footer>
    <!--End footer-main-->
</template>

<script>
export default {
    name: 'FooterComponent',
}
</script>

<style scoped>
.footerlogo-icon{
    height: 40px;
    margin-top: -30px;
}
.logo-text {
  font-family: monospace;
  font-size: 30px;
  margin-left: 6px;
  color: #fff;
  font-weight: bold;
}
.hpform{
    border-radius: 0;
}
</style>