<template>
  <form action="">
	<input v-model="bookName" :class="bookNameFieldError ? 'error' : ''" class="form-field" type="text" name="name" id="name" placeholder="Book name">
	<input v-model="bookAuthor" :class="bookAuthorFieldError ? 'error' : ''" class="form-field" type="text" name="author" id="author" placeholder="Book author">
    <input @click.prevent="submitForm" class="button-submit" type="submit" value="Add book">
	<div v-if="errorMessagesExists" class="error-messages">
		<p v-for="(errorMessage, i) in errorMessages" :key="i" >{{ errorMessage }}</p>
	</div>
  </form>
</template>

<script>
export default {
  name: 'BookForm',
  data() {
	return {
		bookName: '',
		bookAuthor: '',
		bookNameFieldError: false,
		bookAuthorFieldError: false,
		errorMessagesExists: false,
		errorMessages: {
			bookNameField: '',
			bookAuthorField: ''
		}
	};
  },
  methods: {
	submitForm() {
		if (this.bookName.trim() === '') {
			this.bookNameFieldError = true;
			this.errorMessages.bookNameField = 'Fill book name';
		} else {
			this.bookNameFieldError = false;
			this.errorMessages.bookNameField = '';
		}

		if (this.bookAuthor.trim() === '') {
			this.bookAuthorFieldError = true;
			this.errorMessages.bookAuthorField = 'Fill author';
		} else {
			this.bookAuthorFieldError = false;
			this.errorMessages.bookAuthorField = '';
		}

		this.errorMessagesExists = this.isErrorMessagesExists();

		if (this.errorMessagesExists) {
			return;
		}

		let newBook = {
			bookName: this.bookName,
			bookAuthor: this.bookAuthor
		};

		this.$emit('add-new-book', newBook);
	},
	isErrorMessagesExists() {
		let values = Object.values(this.errorMessages).filter((item) => {
			return item.trim() !== "";
		});

		if (values.length > 0) {
			return true;
		}

		return false;
	}
  }
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

	input.button-submit:hover {
		background: #07cc82
	}

	input.error {
		border: 1px solid red;
		background: #ffefef
	}

	.error-messages {
		margin: 20px;
		color: red
	}

</style>

