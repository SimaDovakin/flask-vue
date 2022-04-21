<template>
  <div class="container">
    <h1>Book Manager</h1>
    <BookList/>
  </div>
</template>

<script>
import BookList from './components/BookList.vue'

export default {
  name: 'App',
  components: {
    BookList
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
