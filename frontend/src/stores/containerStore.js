import { defineStore }  from "pinia";

export const useContainerStore = defineStore('containers', {
    state: () => ({
        list: []
    }),
    actions: {
        /**
         * @param {list} containers 
         */
        setContainers(containers) {
            this.list = containers
        },
        
        updateContainers(container) {
            const idFound = this.list.findIndex(c => c.id === container.id)
            if (idFound >= 0) {
                this.list[idFound] = { ...this.list[idFound], ...container} /**This updates (spread operator) a container when found */
            } else {
                this.list.push(container)
            }
        },

        updateContainerStatus(id, status) {
            const idFound = this.list.findIndex(c => c.id === id)
            switch (status){
                case "start":
                    this.list[idFound].status = "running";
                    break;
                case "stop":
                    this.list[idFound].status = "stopping...";
                    break;
                case "die":
                    this.list[idFound].status = "exited";
                    break;
            }
        },

        deleteContainers(deleteId) {
            this.list = this.list.filter(c => c.id !== deleteId)
        }
    }
})