<template>
  <v-app>
    <!-- <v-app-bar
      color="primary"
      dark

    >
    <img src="./assets/AI DENTIST LOGO.jpg" alt="" srcset="" width="80" height="80">
    <p class="text-h6 text-md-h5 text-lg-h4 ml-4"> Aidentist: X-ray Classifier</p>
    
    </v-app-bar> -->
    <v-card elavation="2" color="primary" class="pa-2" height="90" dark>
      <div class="mt-4 ml-4">
      <v-row>
        <img src="./assets/AI DENTIST LOGO.jpg" alt="" srcset="" width="60" height="60" class="mb-0">
        <p class="text-h6 text-md-h5 text-lg-h4 ml-4"> Aidentist: RGB Classifier</p>
      </v-row>
      <p class="ml-15" style="margin-top: -20px; margin-left: 30px;">Tooth anomaly detector for RGB dental images.</p>
    </div>
    </v-card>

    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    //
  }),
};
</script>
