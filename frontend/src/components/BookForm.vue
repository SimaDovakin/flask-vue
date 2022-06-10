<template>
  <form action="">
	<input class="form-field" type="text" name="name" id="name" placeholder="Book name">
	<input class="form-field" type="text" name="author" id="author" placeholder="Book author">
    <input @click.prevent="" class="button-submit" type="submit" value="Add book">
  </form>
</template>

<script>
export default {
  name: 'BookForm',
}
</script>

<style scoped>
	form {
		position: relative;
		display: flex;
		flex-direction: column;
		margin: 30px 20px;
		width: 40%;
		align-items: center;
	}

	form input {
		display: block;
		min-height: 30px
	}
	
	form .form-field {
		margin: 10px 20px;
		padding: 6px;
		width: 100%;
		background: #effff7;
		border: 1px solid #01b974;
		outline: none;
	}

	form .form-field::placeholder {
		color: #01b974;
	}

	input.button-submit {
		width: 60%;
		border: none;
		background: #01b974;
		border-radius: none;
		color: white
	}

</style>

