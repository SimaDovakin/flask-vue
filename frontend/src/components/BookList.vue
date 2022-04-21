<template>
  <table>
      <tr class="table-heading">
          <th>Name</th>
          <th>Author</th>
          <th>Adding date</th>
      </tr>
      <tr v-for="book in bookList" :key="book.id">
          <td>{{ book.name }}</td>
          <td>{{ book.author }}</td>
          <td>{{ book.created_at }}</td>
      </tr>
  </table>
</template>

<script>
export default {
  name: 'BookList',
  props: {
    bookList: Array
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 30px;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

table {
  border-collapse: collapse;
  width: 100%
}
.table-heading {
  background: #01b974;
  color: white
}
td, th {
  text-align: left;
  padding: 8px
}
tr:nth-child(even) {
  background: #dbfded
}
</style>
