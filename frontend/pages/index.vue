<template>
  <div class="section">
    <div class="columns is-mobile">
      <div class="box mx-auto">
        <b-button expanded type="is-info" @click="generatePosition">
          generate position
        </b-button>
        <div class="mt-6 map-wrap">
          <client-only>
            <l-map class="rounded" :zoom="3" :center="[55.9464418,8.1277591]">
              <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png" />
            </l-map>
          </client-only>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'HomePage',

  components: {
  },
  data () {
    return {
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      mapOptions: {
        zoomSnap: 0.5
      },
      attribution:
        '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    }
  },
  methods: {
    generatePosition () {

    }
  }
}
</script>

<style>
.map-wrap {
  height: 50vh;
  width: 80vw;
}
.rounded {
  border-radius: 10px;
}
</style>
