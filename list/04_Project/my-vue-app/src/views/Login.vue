<!-- src/views/Login.vue -->
<template>
  <div class="login">
    <h2>登录页面</h2>
    <form @submit.prevent="login">
      <input v-model="username" type="text" placeholder="用户名" />
      <input v-model="password" type="password" placeholder="密码" />
      <button type="submit">登录</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    login() {
      // 这里可以添加登录逻辑
      if (this.username === 'admin' && this.password === '123456') {
        // 登录成功，跳转到首页
        this.$router.push('/index');
      } else {
        alert('用户名或密码错误');
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.login {
  max-width: 300px;
  margin: 40px auto;
  text-align: center;

  input {
    display: block;
    margin: 10px auto;
    padding: 8px;
    width: 100%;
  }

  button {
    padding: 10px;
    background-color: #007bff;
    color: white;
    border: none;
    cursor: pointer;
    &:hover {
      background-color: #0056b3;
    }
  }
}
</style>
