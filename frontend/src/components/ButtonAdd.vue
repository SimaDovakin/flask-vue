<template>
  <button @click="addNewBook" class="add-book">+</button>
</template>

<script>
export default {
  name: 'ButtonAdd',
  methods: {
	addNewBook() {
		this.$emit('add-new-book-state');
	}
  }
} 
</script>

<style scoped>
.add-book {
  margin: 10px 10px;
  width: 60px;
  height: 60px;
  border-radius: 50%;
  border: none;
  font-size: 32px;
  color: white;
  background: #01b974;
}

.add-book:hover {
  background: #07cc82
}

</style>

