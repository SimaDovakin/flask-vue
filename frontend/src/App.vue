<template>
  <div class="container">
    <h1>Book Manager</h1>
    <BookList :bookList="bookList"/>
  </div>
</template>

<script>
import BookList from './components/BookList.vue'

export default {
  name: 'App',
  components: {
    BookList
  },
  data() {
    return {
      bookList: []
    }
  },
  methods: {
    async getBookList() {
      let response = await fetch('http://127.0.0.1:5000', {
        mode: 'cors',
        headers: {
          'Origin': 'http://localhost'
        }
      });
      let data = await response.json();
      console.log(data);

      this.bookList = data;
    }
  },
  mounted() {
    this.getBookList();
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box
}
body {
  font-family: 'Ubuntu mono', Arial
}

h1 {
  text-align: center;
  margin: 20px
}

.container {
  max-width: 1080px;
  margin: 0 auto;
}
</style>
