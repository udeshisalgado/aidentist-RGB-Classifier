<template>
  <div>
    <!-- <v-layout>
      <v-main>
        <v-container fluid> -->
          <v-row class="mx-4 mt-12">
            <v-col cols="4">
              <input ref="fileInput" type="file" @change="pickFile" />
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
              <p><span class="font-weight-black">Label:</span> Caries</p>
                <h3 class="mb-5 text-decoration-underline">Prediction Results</h3>
                <p><span class="font-weight-black">Caries:</span> 99.817 %</p>
                <p><span class="font-weight-black">Non-Caries:</span> 0.158 %</p>
                <p><span class="font-weight-black">Fake-Caries:</span> 0.025 %</p>
            </v-col>
          </v-row>
        <!-- </v-container>
      </v-main>
    </v-layout> -->
  </div>
</template>

<script>
import axios from "axios"
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
      selectedFile: null,
            label: "",
            caries: "",
            non_caries: "",
            f_caries: "",
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
    getapi(){
      axios.get(`http://127.0.0.1:8000/`)
      .then((result)=>{
        console.log("objectobjectobjectobject");
        console.log(result.data);
      })
    },

    uploadFile() {
      const formData = new FormData();
      formData.append('file', this.selectedFile);

      fetch('http://127.0.0.1:8000/upload', {
                    method: 'POST',
                    body: formData,
                })
                .then(response => response.json())
                .then(data => {
                    console.log(">>>>>>>>>>>>>>data>>>>>>>>>>>>>>>>>>>>>");
                    console.log(data);
                    this.label = data.label;
                    this.caries = data.caries;
                    this.non_caries = data.non_caries;
                    this.f_caries = data.f_caries;

                    // Handle the response from the server
                })
                .catch(error => {
                    console.error(error);
                    // Handle any error that occurred during the request
                });
    },
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
        this.selectedFile = event.target.files[0];
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
        this.uploadFile()
      }
  },
  mounted(){
    this.getapi();
  }
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