new Vue({
    el: '#app',
    data: {
        communities: [],
        community: {},
        users: []
    },
    created() {
        // Загрузка списка сообществ при запуске приложения
        this.loadCommunities();
    },
    methods: {
        loadCommunities() {
            // Загрузка списка сообществ
            fetch('/api/communities')
                .then(response => response.json())
                .then(data => {
                    this.communities = data;
                });
        },
        loadCommunity(communityId) {
            // Загрузка информации о сообществе и его участниках
            fetch(`/api/community/${communityId}`)
                .then(response => response.json())
                .then(data => {
                    this.community = data.community;
                    this.users = data.users;
                });
        }
    }
});
