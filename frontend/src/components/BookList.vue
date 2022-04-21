<template>
  <table>
      <tr class="table-heading">
          <th>Name</th>
          <th>Author</th>
          <th>Adding date</th>
      </tr>
      <tr>
          <td>Solaris</td>
          <td>Stanislav Lem</td>
          <td>2022-04-21</td>
      </tr>
      <tr>
          <td>Crime and Punishment</td>
          <td>Fedor Dostoevskiy</td>
          <td>2022-04-21</td>
      </tr>
      <tr>
          <td>Crime and Punishment</td>
          <td>Fedor Dostoevskiy</td>
          <td>2022-04-21</td>
      </tr>
      <tr>
          <td>Crime and Punishment</td>
          <td>Fedor Dostoevskiy</td>
          <td>2022-04-21</td>
      </tr>
  </table>
</template>

<script>
export default {
  name: 'BookList',
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
