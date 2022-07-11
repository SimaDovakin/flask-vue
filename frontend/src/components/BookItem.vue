<template>
	<td>{{ book.name }}</td>
	<td>{{ book.author }}</td>
	<td>{{ book.created_at }}</td>
	<td>
		<button @click="editBook">Edit</button>
		<button @click="deleteBook">Delete</button>
	</td>
</template>

<script>
export default {
  name: 'BookItem',
  props: {
	book: Object
  },
  methods: {
    deleteBook() {
		this.$emit('delete-book', this.book);
    },
	editBook() {
		this.$emit('edit-book', this.book);
	}
  }
}
</script>

<style scoped>
td {
  text-align: left;
  padding: 8px
}
</style>

