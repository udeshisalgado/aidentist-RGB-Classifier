<template>
  <div>
    <!-- <v-layout>
      <v-main>
        <v-container fluid> -->
          <v-row class="mx-4 mt-12">
            <v-col cols="4">
              <input ref="fileInput" type="file" @input="pickFile" />
            </v-col>
            <v-col cols="4">
              <div>
                <v-card width="200" height="200" variant="outlined">
                  <v-img
                  width="200"
                  height="200"
                  aspect-ratio="4/3"
                  cover
                  :src="previewImage"
                ></v-img>
                </v-card>
                
              </div>
            </v-col>
            <v-col cols="4">
              <p><span class="font-weight-black">Label:</span> value</p>
                <h3 class="mb-5 text-decoration-underline">Prediction Result</h3>
                <p><span class="font-weight-black">Caries:</span> value</p>
                <p><span class="font-weight-black">Non-Caries:</span> value</p>
                <p><span class="font-weight-black">Fake-Caries:</span> value</p>
            </v-col>
          </v-row>
        <!-- </v-container>
      </v-main>
    </v-layout> -->
  </div>
</template>

<script>
export default {
  data() {
    return {
      dialog: false,
      file: null,
      imageUrl: "",
      currentImage: undefined,
      // previewImage: undefined,
      previewImage: null,
      imageSelected: false,
    };
  },
  //   watch: {
  //   file(newFile) {
  //     if (newFile) {
  //       this.previewImage(newFile);
  //     }
  //   },
  // },
  methods: {
    // previewImage(file) {
    //   const reader = new FileReader();
    //   reader.onload = () => {
    //     this.imageUrl = reader.result;
    //   };
    //   reader.readAsDataURL(file);
    // },
    // selectImage(image) {
    //   this.currentImage = image;
    //   this.previewImage = URL.createObjectURL(this.currentImage);
    //   this.progress = 0;
    //   this.message = "";
    // },
    selectImage () {
          this.$refs.fileInput.click()
      },
      pickFile () {
        let input = this.$refs.fileInput
        let file = input.files
        if (file && file[0]) {
          let reader = new FileReader
          reader.onload = e => {
            this.previewImage = e.target.result
          }
          reader.readAsDataURL(file[0])
          this.$emit('input', file[0])
        }
      }
  },
};
</script>
<style scoped lang="scss">
.imagePreviewWrapper {
    width: 250px;
    height: 250px;
    display: block;
    cursor: pointer;
    margin: 0 auto 30px;
    background-size: cover;
    background-position: center center;
}
</style>