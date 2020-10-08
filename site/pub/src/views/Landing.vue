<template>
  <div>
    <div class="position-relative">
      <!-- shape Hero -->
      <section class="section-shaped my-0" id="secTop">
        <div class="shape shape-style-1 shape-default shape-skew">
          <span></span>
          <span></span>
          <span></span>
          <span></span>
          <span></span>
          <span></span>
          <span></span>
          <span></span>
          <span></span>
        </div>

        <div class="container shape-container d-flex">
          <div class="col px-0">
            <div class="row">
              <div class="col-lg-6">
                <h1 class="display-3  text-white">
                  {{ $t('app.name') }}
                  {{ $t('app.version') }}
                  <!-- A beautiful Design System -->
                  <span>{{ $t('app.short_description') }}</span>
                </h1>

                <p class="lead text-white">
                  {{ $t('app.description') }}
                </p>

                <div class="btn-wrapper">
                  <router-link to="/login" class="btn btn-white btn-icon">
                    <span class="btn-inner--icon">
                      <i class="fa fa-sign-in mr-2"></i>
                    </span>

                    <span class="nav-link-inner--text">
                      {{ $t('actions.Login button short text') }}
                    </span>
                  </router-link>

                  <router-link to="/register" class="btn btn-white btn-icon">
                    <span class="btn-inner--icon">
                      <i class="fa fa-address-card mr-2"></i>
                    </span>

                    <span class="nav-link-inner--text">
                      {{ $t('actions.Sign up') }}
                    </span>
                  </router-link>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
        <!-- 1st Hero Variation -->
    </div>

    <!-- Descriptor cards -->
    <section class="section section-lg pt-lg-0 mt--200" id="secCards">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-lg-12">
            <div class="row row-grid">
              <div class="col-lg-4">
                <card class="border-0" hover shadow body-classes="py-5">
                  <icon 
                    name="fa fa-thumbs-up" 
                    type="primary" 
                    rounded class="mb-4"
                  />

                  <h6 class="text-primary text-uppercase">
                    {{ $t('sections.cards.one.title') }}
                  </h6>

                  <p class="description mt-3">
                    {{ $t('sections.cards.one.text') }}
                  </p>

                  <div>
                    <badge type="primary" rounded>
                      {{ $t('sections.cards.one.badges.one') }}
                    </badge>

                    <badge type="primary" rounded>
                      {{ $t('sections.cards.one.badges.two') }}
                    </badge>

                    <badge type="primary" rounded>
                      {{ $t('sections.cards.one.badges.three') }}
                    </badge>
                  </div>

                  <base-button tag="a" href="#" type="primary" class="mt-4">
                    {{ $t('actions.Read more') }}
                  </base-button>
                </card>
              </div>

              <div class="col-lg-4">
                <card class="border-0" hover shadow body-classes="py-5">
                  <icon 
                    name="fa fa-book" 
                    type="success" 
                    rounded class="mb-4"
                  />

                  <h6 class="text-success text-uppercase">
                    {{ $t('sections.cards.two.title') }}
                  </h6>

                  <p class="description mt-3">
                    <i18n path="sections.cards.two.text">
                      <a
                        href="https://www.abebooks.com/servlet/BookDetailsPL?bi=30357495783"
                        target="_blank"
                      >(2000, Pierre P.)</a>
                    </i18n>
                  </p>

                  <div>
                    <badge type="success" rounded>
                      {{ $t('sections.cards.two.badges.one') }}
                    </badge>

                    <badge type="success" rounded>
                      {{ $t('sections.cards.two.badges.two') }}
                    </badge>

                    <badge type="success" rounded>
                      {{ $t('sections.cards.two.badges.three') }}
                    </badge>
                  </div>

                  <base-button tag="a" href="#" type="success" class="mt-4">
                    {{ $t('actions.Read more') }}
                  </base-button>
                </card>
              </div>

              <div class="col-lg-4">
                <card class="border-0" hover shadow body-classes="py-5">
                  <icon 
                    name="ni ni-paper-diploma"
                    type="warning" 
                    rounded class="mb-4"
                  />

                  <h6 class="text-warning text-uppercase">
                    {{ $t('sections.cards.three.title') }}
                  </h6>

                  <p class="description mt-3">
                    {{ $t('sections.cards.three.text') }}
                  </p>

                  <div>
                    <badge type="warning" rounded>
                      {{ $t('sections.cards.three.badges.one') }}
                    </badge>

                    <badge type="warning" rounded>
                      {{ $t('sections.cards.three.badges.two') }}
                    </badge>

                    <badge type="warning" rounded>
                      {{ $t('sections.cards.three.badges.three') }}
                    </badge>
                  </div>

                  <base-button tag="a" href="#" type="warning" class="mt-4">
                    {{ $t('actions.Read more') }}
                  </base-button>
                </card>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-lg" id="secFeatures">
      <div class="container">
        <div class="row row-grid align-items-center">
          <div class="col-md-6 order-md-2">
            <img src="img/theme/promo-1.png" class="img-fluid floating">
          </div>

          <div class="col-md-6 order-md-1">
            <div class="pr-md-5">
              <icon 
                name="ni ni-settings-gear-65" 
                class="mb-5" 
                size="lg" 
                type="success" 
                shadow
                rounded
              >
              </icon>

              <h3>{{ $t('sections.features.title') }}</h3>

              <p>
                {{ $t('sections.features.text') }}
              </p>

              <ul class="list-unstyled mt-5">
                <li class="py-2">
                  <div class="d-flex align-items-center">
                    <badge
                      type="success"
                      circle class="mr-3"
                      icon="ni ni-curved-next"
                    />

                    <h6 class="mb-0">
                      {{ $t('sections.features.list.one') }}
                    </h6>
                  </div>
                </li>

                <li class="py-2">
                  <div class="d-flex align-items-center">
                    <badge
                      type="success"
                      circle class="mr-3"
                      icon="fa fa-cogs"
                    />

                    <h6 class="mb-0">
                      {{ $t('sections.features.list.two') }}
                    </h6>
                  </div>
                </li>

                <li class="py-2">
                  <div class="d-flex align-items-center">
                    <badge
                      type="success"
                      circle class="mr-3"
                      icon="ni ni-button-play"
                    />

                    <h6 class="mb-0">
                      {{ $t('sections.features.list.three') }}
                    </h6>
                  </div>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section bg-secondary" id="secRDI">
      <div class="container">
        <div class="row row-grid align-items-center">
          <div class="col-md-4">
            <div class="card bg-default shadow border-0">
              <img
                v-lazy="'img/theme/img-1-1200x1000.jpg'"
                class="card-img-top"
              />

              <blockquote class="card-blockquote">
                <svg
                  preserveAspectRatio="none"
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 583 95"
                  class="svg-bg"
                >
                  <polygon
                    points="0,52 583,95 0,95" 
                    class="fill-default" 
                  />

                  <polygon
                    points="0,42 583,95 683,0 0,95"
                    opacity=".2"
                    class="fill-default"
                  />
                </svg>

                <h4
                  class="display-3 font-weight-bold text-white"
                >
                  {{ $t('sections.RDI.research.title') }}
                </h4>

                <p class="lead text-italic text-white">
                  <i18n path="sections.RDI.research.text">
                    <a
                      href="https://www.nsf.gov/statistics/randdef/rd-definitions.pdf"
                      target="_blank"
                    >1</a>
                  </i18n>
                </p>
              </blockquote>
            </div>
          </div>

          <div class="col-md-4">
            <div class="pl-md-5">
              <!-- <icon
                name="ni ni-settings"
                class="mb-5"
                size="lg"
                type="warning"
                shadow rounded
              /> -->

              <h3>
                {{ $t('sections.RDI.dev.title') }}
              </h3>

              <p class="lead">
                <i18n path="sections.RDI.dev.text1">
                  <a
                    href="https://www.nsf.gov/statistics/randdef/rd-definitions.pdf"
                    target="_blank"
                  >1</a>
                </i18n>
              </p>

              <p>
                <i18n path="sections.RDI.dev.text2">
                  <a
                    href="http://www.ejournal.unam.mx/rca/208/RCA20801.pdf"
                    target="_blank"
                  >2</a>
                </i18n>
              </p>

              <!-- <a href="#" class="font-weight-bold text-warning mt-5">
                A beautiful UI Kit for impactful websites
              </a> -->
            </div>
          </div>

          <div class="col-md-4">
            <div class="pl-md-5">
              <!-- <icon
                name="ni ni-settings"
                class="mb-5"
                size="lg"
                type="warning"
                shadow rounded
              /> -->

              <h3>
                {{ $t('sections.RDI.innovation.title') }}
              </h3>

              <p class="lead">
                <i><q>{{ $t('sections.RDI.innovation.text1') }}</q></i>
                [<a
                    href="http://www.ejournal.unam.mx/rca/208/RCA20801.pdf"
                    target="_blank"
                  >2</a>]
              </p>

              <p>
                <i><q>{{ $t('sections.RDI.innovation.text2') }}</q></i>
                [<a
                    href="http://www.ejournal.unam.mx/rca/208/RCA20801.pdf"
                    target="_blank"
                  >2</a>]
              </p>

              <!-- <a href="#" class="font-weight-bold text-warning mt-5">
                A beautiful UI Kit for impactful websites
              </a> -->
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section section section-shaped my-0 overflow-hidden" id="secTech">
      <div class="shape shape-style-1 bg-gradient-warning shape-skew">
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
      </div>

      <div class="container py-0">
        <div class="row row-grid align-items-center">
          <div class="col-md-6 order-lg-2 ml-lg-auto">
            <div class="position-relative pl-md-5">
              <img src="img/ill/ill-2.svg" class="img-center img-fluid">
            </div>
          </div>

          <div class="col-lg-6 order-lg-1">
            <div class="d-flex px-3">
              <div>
                <!-- <icon
                  name="ni ni-bulb-61"
                  size="lg"
                  class="bg-gradient-white"
                  color="primary"
                  shadow
                  rounded
                />
                <icon
                  name="ni ni-diamond"
                  size="lg"
                  class="bg-gradient-white"
                  color="primary"
                  shadow
                  rounded
                />
                <icon
                  name="ni ni-palette"
                  size="lg"
                  class="bg-gradient-white"
                  color="primary"
                  shadow
                  rounded
                />
                <icon
                  name="ni ni-planet"
                  size="lg"
                  class="bg-gradient-white"
                  color="primary"
                  shadow
                  rounded
                />
                <icon
                  name="ni ni-settings-gear-65"
                  size="lg"
                  class="bg-gradient-white"
                  color="primary"
                  shadow
                  rounded
                /> -->
                <icon
                  name="ni ni-settings"
                  size="lg"
                  class="bg-gradient-white"
                  color="primary"
                  shadow
                  rounded
                />
              </div>

              <div class="pl-4">
                <h4 class="display-3 text-white">
                  {{ $t('sections.tech.title') }}
                </h4>

                <p class="text-white">
                  {{ $t('sections.tech.text') }}
                </p>
              </div>
            </div>

            <card shadow class="shadow-lg--hover mt-5">
              <div class="d-flex">
                <!-- <div>
                  <icon
                    name="ni ni-satisfied"
                    gradient="success"
                    color="white"
                    shadow
                    rounded
                  />
                </div> -->

                <div>
                  <h5 class="title text-success">
                    {{ $t('sections.tech.cards.one.title') }}
                  </h5>

                  <p>
                    <i><q>{{ $t('sections.tech.cards.one.text') }}</q></i>
                    &nbsp;[<a
                        href="https://es-vuejs.github.io/vuejs.org/v2/guide/"
                        target="_blank"
                      >3</a>]
                  </p>

                  <a
                    href="https://es-vuejs.github.io/vuejs.org/v2/guide/"
                    class="text-success"
                    target="_blank"
                  >
                    {{ $t('actions.Read more') }}
                  </a>
                </div>
              </div>
            </card>

            <card shadow class="shadow-lg--hover mt-5">
              <div class="d-flex">
                <!-- <div>
                  <icon
                    name="ni ni-active-40"
                    gradient="warning"
                    color="white"
                    shadow
                    rounded
                  />
                </div> -->

                <div>
                  <h5 class="title text-warning">
                    {{ $t('sections.tech.cards.two.title') }}
                  </h5>

                  <p>
                    <i><q>{{ $t('sections.tech.cards.two.text') }}</q></i>
                    &nbsp;[<a
                        href="https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Introducci%C3%B3n"
                        target="_blank"
                      >4</a>]
                  </p>

                  <a
                    href="https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Introducci%C3%B3n"
                    class="text-warning"
                    target="_blank"
                  >
                    {{ $t('actions.Read more') }}
                  </a>
                </div>
              </div>
            </card>
          </div>
        </div>
      </div>
    </section>

    <!-- <section class="section section-lg" id="secTestimonials">
      <div class="container">
        <div class="row justify-content-center text-center mb-lg">
          <div class="col-lg-8">
            <h2 class="display-3">
              {{ $t('sections.testimonials.title') }}
            </h2>

            <p class="lead text-muted">
              {{ $t('sections.testimonials.text') }}
            </p>
          </div>
        </div>

        <div class="row">
          <div class="col-md-6 col-lg-3 mb-5 mb-lg-0">
            <div class="px-4">
              <img
                v-lazy="'img/theme/team-1-800x800.jpg'"
                class="rounded-circle img-center img-fluid shadow shadow-lg--hover"
                style="width: 200px;"
              />

              <div class="pt-4 text-center">
                <h5 class="title">
                  <span class="d-block mb-1">
                    {{ $t('sections.testimonials.one.name') }}
                  </span>

                  <small class="h6 text-muted">
                    {{ $t('sections.testimonials.one.role') }}
                  </small>
                </h5>

                <div class="mt-3">
                  <base-button
                    tag="a"
                    :href="$t('sections.testimonials.one.twitter')"
                    type="warning"
                    icon="fa fa-twitter"
                    rounded
                    icon-only
                  />

                  <base-button
                    tag="a"
                    :href="$t('sections.testimonials.one.fb')"
                    type="warning"
                    icon="fa fa-facebook"
                    rounded
                    icon-only
                  />
                </div>
              </div>
            </div>
          </div>

          <div class="col-md-6 col-lg-3 mb-5 mb-lg-0">
            <div class="px-4">
              <img
                v-lazy="'img/theme/team-2-800x800.jpg'"
                class="rounded-circle img-center img-fluid shadow shadow-lg--hover"
                style="width: 200px;"
              />

              <div class="pt-4 text-center">
                <h5 class="title">
                  <span class="d-block mb-1">
                    {{ $t('sections.testimonials.two.name') }}
                  </span>

                  <small class="h6 text-muted">
                    {{ $t('sections.testimonials.two.role') }}
                  </small>
                </h5>

                <div class="mt-3">
                  <base-button
                    tag="a"
                    :href="$t('sections.testimonials.two.twitter')"
                    type="primary"
                    icon="fa fa-twitter"
                    rounded
                    icon-only
                  />

                  <base-button
                    tag="a"
                    :href="$t('sections.testimonials.two.fb')"
                    type="primary"
                    icon="fa fa-facebook"
                    rounded
                    icon-only
                  />
                </div>
              </div>
            </div>
          </div>

          <div class="col-md-6 col-lg-3 mb-5 mb-lg-0">
            <div class="px-4">
              <img
                v-lazy="'img/theme/team-3-800x800.jpg'"
                class="rounded-circle img-center img-fluid shadow shadow-lg--hover"
                style="width: 200px;"
              />

              <div class="pt-4 text-center">
                <h5 class="title">
                  <span class="d-block mb-1">
                    {{ $t('sections.testimonials.three.name') }}
                  </span>

                  <small class="h6 text-muted">
                    {{ $t('sections.testimonials.three.role') }}
                  </small>
                </h5>

                <div class="mt-3">
                  <base-button
                    tag="a"
                    :href="$t('sections.testimonials.three.twitter')"
                    type="info"
                    icon="fa fa-twitter"
                    rounded
                    icon-only
                  />

                  <base-button
                    tag="a"
                    :href="$t('sections.testimonials.fb.twitter')"
                    type="info"
                    icon="fa fa-facebook"
                    rounded
                    icon-only
                  />
                </div>
              </div>
            </div>
          </div>

          <div class="col-md-6 col-lg-3 mb-5 mb-lg-0">
            <div class="px-4">
              <img
                v-lazy="'img/theme/team-4-800x800.jpg'"
                class="rounded-circle img-center img-fluid shadow shadow-lg--hover"
                style="width: 200px;"
              />

              <div class="pt-4 text-center">
                <h5 class="title">
                  <span class="d-block mb-1">
                    {{ $t('sections.testimonials.four.name') }}
                  </span>

                  <small class="h6 text-muted">
                    {{ $t('sections.testimonials.four.role') }}
                  </small>
                </h5>

                <div class="mt-3">
                  <base-button
                    tag="a"
                    :href="$t('sections.testimonials.four.twitter')"
                    type="info"
                    icon="fa fa-twitter"
                    rounded
                    icon-only
                  />

                  <base-button
                    tag="a"
                    :href="$t('sections.testimonials.four.twitter')"
                    type="info"
                    icon="fa fa-facebook"
                    rounded
                    icon-only
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section> -->

    <section class="section section-shaped my-0 overflow-hidden" id="secServices">
      <div class="shape shape-style-3 bg-gradient-default shape-skew">
        <span></span>
        <span></span>
        <span></span>
        <span></span>
      </div>

      <div class="container pt-lg pb-300">
        <div class="row text-center justify-content-center">
          <div class="col-lg-10">
            <h2 class="display-3 text-white">
              {{ $t('sections.services.title') }}
            </h2>

            <p class="lead text-white">
              {{ $t('sections.services.text') }}:
            </p>
          </div>
        </div>

        <div class="row row-grid mt-5">
          <div class="col-lg-4">
            <icon
              name="ni ni-settings"
              size="lg"
              gradient="white"
              shadow
              round
              color="primary"
            />

            <h5 class="text-white mt-3">
              {{ $t('sections.services.one.title') }}
            </h5>

            <p class="text-white mt-3">
              {{ $t('sections.services.one.text') }}.
            </p>
          </div>

          <div class="col-lg-4">
            <icon
              name="ni ni-ruler-pencil"
              size="lg"
              gradient="white"
              shadow
              round
              color="primary"
            />

            <h5 class="text-white mt-3">
              {{ $t('sections.services.two.title') }}
            </h5>

            <p class="text-white mt-3">
              {{ $t('sections.services.two.text') }}.
            </p>
          </div>

          <div class="col-lg-4">
            <icon
              name="ni ni-atom"
              size="lg"
              gradient="white"
              shadow
              round
              color="primary"
            />

            <h5 class="text-white mt-3">
              {{ $t('sections.services.three.title') }}
            </h5>

            <p class="text-white mt-3">
              {{ $t('sections.services.three.text') }}.
            </p>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-lg pt-lg-0 section-contact-us" id="secContact">
      <div class="container">
        <div class="row justify-content-center mt--300">
          <div class="col-lg-8">
            <card gradient="secondary" shadow body-classes="p-lg-5">
              <h4 class="mb-1">
                {{ $t('sections.contact.title') }}
              </h4>

              <p class="mt-0">
                {{ $t('sections.contact.text') }}
              </p>

              <base-input
                class="mt-5"
                alternative
                :placeholder="$t('Full name')"
                addon-left-icon="ni ni-user-run"
              />

              <base-input
                alternative
                :placeholder="$t('E-mail')"
                addon-left-icon="ni ni-email-83"
              />

              <base-input class="mb-4">
                <textarea
                  class="form-control form-control-alternative"
                  name="name"
                  rows="4"
                  cols="80"
                  :placeholder="$t('forms.contact.fields.Write your message here')"
                />
              </base-input>

              <base-button type="default" round block size="lg">
                {{ $t('actions.Send') }}
              </base-button>
            </card>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-lg" id="secColab">
      <div class="container">
        <div class="row row-grid justify-content-center">
          <div class="col-lg-8 text-center">
            <h2 class="display-3">
              {{ $t('sections.colab.title') }}
              <span class="text-success">
                {{ $t('sections.colab.subtitle') }}
              </span>
            </h2>

            <p class="lead">
              {{ $t('sections.colab.text') }}
            </p>

            <div class="btn-wrapper">
              <a 
                href="mailto:edario_ram@hotmail.com?subject=Deseo colaborar con..."
                class="btn btn-primary mb-3 mb-sm-0"
              >
                {{ $t('sections.colab.join us') }}
              </a>
            </div>

            <div class="text-center">
              <h4 class="display-4 mb-5 mt-5">
                {{ $t('sections.providers.title') }}
              </h4>

              <div class="row justify-content-center">
                <div class="col-lg-3 col-3">
                  <a
                    href="https://www.nasa.gov/"
                    target="_blank"
                    data-toggle="tooltip"
                    data-original-title="National Aeronautics and Space Administration"
                  >
                    <img
                      v-lazy="'https://www.nasa.gov/sites/all/themes/custom/nasatwo/images/nasa-logo.svg'"
                      class="img-fluid"
                    />
                  </a>
                </div>

                <div class="col-lg-4 col-4">
                  <a 
                    href="https://about.google/"
                    target="_blank"
                    data-toggle="tooltip"
                    data-original-title="Google - Acerca de"
                  >
                    <img
                      v-lazy="'https://www.google.com.mx/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png'"
                      class="img-fluid"
                    />
                  </a>
                </div>

                <div class="col-lg-4 col-4">
                  <a
                    href="https://www.python.org/"
                    target="_blank"
                    data-toggle="tooltip"
                    data-original-title="Python, programming language"
                  >
                    <img
                      v-lazy="'https://www.python.org/static/img/python-logo.png'"
                      class="img-fluid"
                    />
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <a
      @click="goToTop()"
      ref="btnGoToTop"
      id="btnGoToTop"
      :title="$t('Top')"
      @mouseenter="typeIconUp = 'success'"
      @mouseleave="typeIconUp = 'primary'"
    >
      <icon 
        name="ni ni-bold-up"
        :type="typeIconUp" 
        rounded 
        ref="iconUp"
        id="iconUp"
        class="mb-4"
      />
    </a> 
  </div>
</template>

<script>
  export default {
    name: "home",
    components: {},
    data () {
      return {
        typeIconUp: "primary",
      }
    },
    methods: {
      goToTop () {
        document.body.scrollTop = 0 // For Safari
        document.documentElement.scrollTop = 0 // For Chrome, Firefox, IE and Opera
      },

      handleScroll (event) {
        if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
          this.$refs.btnGoToTop.style.display = "block"
        } else {
          this.$refs.btnGoToTop.style.display = "none"
        }
      },
    },
    created () {
      window.addEventListener('scroll', this.handleScroll)
    },
    mounted () {
      //window.onscroll = this._evalScroll()
    },
    destroyed () {
      window.removeEventListener('scroll', this.handleScroll);
    }
  }
</script>

<style scoped>
  #btnGoToTop {
    display: none; /* Hidden by default */
    position: fixed; /* Fixed/sticky position */
    bottom: 80px; /* Place the button at the bottom of the page */
    right: 30px; /* Place the button 30px from the right */
    z-index: 99; /* Make sure it does not overlap */
    cursor: pointer;
  }
</style>