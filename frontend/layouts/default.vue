<template>
  <div class="sea-cover">
    <div class="section">
      <div class="container">
        <div class="has-text-white is-size-1 is-flex is-justify-content-center">
          <Logo />
          Find You Sea
        </div>
      </div>
    </div>
    <Nuxt />
  </div>
</template>

<script>
import Logo from '~/components/Logo.vue'
export default {
  components: { Logo },
  data () {
    return {

    }
  },
  mounted () {
    if (localStorage.getItem('access')) {
      this.$store.commit('auth/authenticated', true)
    }
  }
}
</script>

<style>
.sea-cover {
  background-image: url(~/assets/img/johannes-plenio-boat.jpg);
  background-size: cover;
  background-position: center center;

  min-height: 100vh;
}
</style>
