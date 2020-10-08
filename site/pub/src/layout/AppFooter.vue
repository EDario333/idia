<template>
  <!-- <footer class="footer has-cards"> -->
  <footer>
    <!-- <div class="container container-lg">
      <div class="row">
        <div class="col-md-6 mb-5 mb-md-0">
          <div class="card card-lift--hover shadow border-0">
            <router-link to="/landing" title="Landing Page">
              <img v-lazy="'img/theme/landing.jpg'" class="card-img">
            </router-link>
          </div>
        </div>

        <div class="col-md-6 mb-5 mb-lg-0">
          <div class="card card-lift--hover shadow border-0">
            <router-link to="/profile" title="Profile Page">
              <img v-lazy="'img/theme/profile.jpg'" class="card-img">
            </router-link>
          </div>
        </div>
      </div>
    </div> -->

    <div class="container">
      <div class="row row-grid align-items-center my-md">
        <div class="col-lg-6">
          <h3 class="text-primary font-weight-light mb-2">
            {{ $t('sections.footer.title') }}
          </h3>

          <h4 class="mb-0 font-weight-light">
            {{ $t('sections.footer.subtitle') }}
          </h4>
        </div>

        <div class="col-lg-6 text-lg-center btn-wrapper">
          <a 
            target="_blank"
            rel="noopener"
            href="https://twitter.com/EdgarRa90028538"
            class="btn btn-neutral btn-icon-only btn-twitter btn-round btn-lg"
            data-toggle="tooltip"
            :data-original-title="$t('Follow me on Twitter')"
            :title="$t('Follow me on Twitter')"
          >
            <i class="fa fa-twitter"></i>
          </a>

          <a
            target="_blank"
            rel="noopener"
            href="https://github.com/EDario333"
            class="btn btn-neutral btn-icon-only btn-github btn-round btn-lg"
            data-toggle="tooltip"
            :data-original-title="$t('Star me on Github')"
            :title="$t('Star me on Github')"
          >
            <i class="fa fa-github"></i>
          </a>
        </div>
      </div>

      <hr>

      <div class="row align-items-center justify-content-md-between">
        <div class="col-md-6">
          <div class="copyright">
            &copy; {{year}}
            <a 
              href="https://github.com/EDario333"
              target="_blank"
              rel="noopener"
            >
              EDar&iacute;o
            </a>
          </div>
        </div>

        <div class="col-md-6">
          <ul class="nav nav-footer justify-content-end">
            <li class="nav-item">
              <a
                href="https://mit-license.org/"
                class="nav-link"
                target="_blank"
                rel="noopener"
              >
                MIT License
              </a>
            </li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Docs 4 cookie notice: -->
    <!-- https://github.com/apertureless/vue-cookie-law -->
    <!-- <cookie-law
      theme="blood-orange"
      :buttonText="$t('I agree')"
      buttonLink="aldo"
      :buttonLinkText="$t('actions.Read more')"
    > -->
    <cookie-law
      theme="blood-orange"
      :buttonText="$t('I agree')"
    >
      <div slot="message">
        <i18n path="Cookie notice">
          <a
            href="https://www.nsf.gov/statistics/randdef/rd-definitions.pdf"
            target="_blank"
          >
            {{ $t('Cookie policy') }}
          </a>
        </i18n>
      </div>
    </cookie-law>
  </footer>
</template>

<script>
  import CookieLaw from 'vue-cookie-law'

  export default {
    name: 'app-footer',
    components: { CookieLaw },
    data() {
      return {
        year: new Date().getFullYear()
      }
    }
  };
</script>

<style>
  .Cookie--blood-orange .Cookie__button {
    border-radius: 10px;
  }
</style>
