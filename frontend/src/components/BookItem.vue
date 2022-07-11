<template>
	<td>{{ book.name }}</td>
	<td>{{ book.author }}</td>
	<td>{{ book.created_at }}</td>
	<td>
		<button>Edit</button>
		<button>Delete</button>
	</td>
</template>

<script>
export default {
  name: 'BookItem',
  props: {
	book: Object
  } 
}
</script>

<style scoped>
td {
  text-align: left;
  padding: 8px
}
</style>

