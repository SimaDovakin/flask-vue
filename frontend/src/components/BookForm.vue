<template>
  <form action="">
    <label for="name">Book name</label>
    <input type="text" name="name" id="name">
    <label for="author">Book author</label>
    <input type="text" name="author" id="author">
    <input type="submit" value="Add book">
  </form>
</template>

<script>
export default {
  name: 'BookForm'
}
</script>

