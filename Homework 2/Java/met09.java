public class met09 {
    public class Cat {
        private String name;
        private String owner;

        public Cat(String name, String owner) {
            this.name = name;
            this.owner = owner;
        }

        public String getName() {
            return this.name;
        }

        public String getOwner() {
            return this.owner;
        }

        public void changeName(String newName) {
            this.name = newName;
        }
        
        public void changeOwner(String newOwner) {
            this.owner = newOwner;
        }

        @Override
        public boolean equals(Object other) {
            if (other == this) {
                return true;
            }

            if (!(other instanceof Cat)) {
                return false;
            }

            Cat otherCat = (Cat)other;
            return otherCat.getName().equals(this.name) && otherCat.getOwner().equals(this.owner);
        }

        @Override
        public int hashCode() {
            int hash = 11;
            hash = 51 * hash + this.name.hashCode() + this.owner.hashCode();
            return hash;
        }
    }

    public static void main(String[] args) {
        met09 demo = new met09();
        Cat cat1 = demo.new Cat("Garfield", "Jon");
        Cat cat2 = demo.new Cat("Felix", "Jeff");
        System.out.println(cat1.equals(cat2)); // False
        cat2.changeName("Garfield");
        cat2.changeOwner("Jon");
        System.out.println(cat1.equals(cat2)); // True
    }
}
