<template>
  <div>
    <section class="main-content columns">
      <div class="container column is-10">
        <Nuxt />
      </div>
    </section>
  </div>
</template>

<script>
export default {
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
