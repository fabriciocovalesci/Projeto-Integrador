<template>
  <div>
    <div>
      <h2 class="contato">Contato</h2>
    </div>

    <div class="campos-principal titulo">
      <b-form @submit="onSubmit" @reset="onReset" v-if="show">
        <b-form-group id="input-group-1" label="Email:" label-for="input-1">
          <b-form-input
            class="campos"
            id="input-1"
            v-model="form.email"
            type="email"
            required
            placeholder="Seu email ..."
          >
          </b-form-input>
        </b-form-group>

        <b-form-group
          id="input-group-2"
          label="Nome Completo:"
          label-for="input-2"
        >
          <b-form-input
            class="campos"
            id="input-2"
            v-model="form.name"
            required
            placeholder="Seu nome ..."
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-3" label="Assunto:" label-for="input-3">
          <b-form-input
            class="campos"
            id="input-3"
            v-model="form.name"
            required
            placeholder="Assunto ..."
          ></b-form-input>
        </b-form-group>

        <p class="titulo">Deixe seu comentário</p>
        <b-form-textarea
          id="textarea-no-resize"
          placeholder="Seu comentário é importante para nós ..."
          rows="5"
          no-resize
        ></b-form-textarea>

        <b-button
          type="submit"
          class="mt-4 p-2 mb-3 botao"
          pill
          variant="primary"
          >Enviar</b-button
        >
      </b-form>
    </div>
  </div>
</template>

<script>
export default {
  name: "contato",
  data() {
    return {
      form: {
        email: "",
        name: "",
        food: null,
        checked: []
      },
      foods: [
        { text: "Select One", value: null },
        "Carrots",
        "Beans",
        "Tomatoes",
        "Corn"
      ],
      show: true
    };
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      alert(JSON.stringify(this.form));
    },
    onReset(evt) {
      evt.preventDefault();
      // Reset our form values
      this.form.email = "";
      this.form.name = "";
      this.form.food = null;
      this.form.checked = [];
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    }
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=ABeeZee&display=swap");

.contato {
  font-family: "ABeeZee", sans-serif;
  text-align: center;
  color: #2c1c0d;
  padding: 10px;
  margin-top: 64px;
}
.titulo {
  font-family: "ABeeZee", sans-serif;
  text-align: center;
  color: #2c1c0d;
  padding: 10px;
}

.campos-principal {
  display: flex;
  flex-direction: column;
  align-content: center;
}
.campos {
  width: 60%;
  height: 40px;
  margin: 0 auto;
  padding: 15px;
}

.botao {
  width: 20%;
}
</style>
