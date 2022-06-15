<template>
  <div class="container">
    <h1>Book Manager</h1>
    <BookList :bookList="bookList"/>
	<div class="form-container">
		<ButtonAdd @add-new-book-state="addNewBookState" v-if="generalState === 'viewBookList'" :generalState="generalState" />
		<BookForm @add-new-book="addNewBook" v-if="generalState !== 'viewBookList'" />
	</div>
  </div>
</template>

<script>
import BookList from './components/BookList.vue'
import ButtonAdd from './components/ButtonAdd.vue'
import BookForm from './components/BookForm.vue'

export default {
  name: 'App',
  components: {
    BookList,
	ButtonAdd,
	BookForm
  },
  data() {
    return {
		generalState: 'viewBookList', // General state of app. Can acept following values: 'viewBookList', 'addNewBook' and 'editBook' 
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
    },
	addNewBookState() {
		this.generalState = 'addNewBook';
	},
	async addNewBook(newBook) {
		console.log("NEW BOOK");
		console.log(newBook);

		let postData = {
			name: newBook.bookName,
			author: newBook.bookAuthor
		};

		await fetch('http://127.0.0.1:5000/create', {
			method: 'POST',
			mode: 'cors',
			headers: {
				'Origin': 'http://localhost',
				'Accept': 'application/json',
				'Content-type': 'application/json'
			},
			body: JSON.stringify(postData)
		});

		this.generalState = 'viewBookList';
		this.getBookList();
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

.form-container {
	display: flex;
	flex-direction: column;
	align-items: center
}
</style>
