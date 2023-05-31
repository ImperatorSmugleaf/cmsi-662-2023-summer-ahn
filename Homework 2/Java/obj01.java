public class obj01 {
    public class Dog {
        private String name;
    
        public Dog(String name) {
            this.name = name;
        }
    
        public String getName() {
            return this.name;
        }
    
        public void rename(String newName) {
            this.name = newName;
        }

        public void speak() {
            System.out.println("Bark!");
        }
    }
    
    public static void main(String[] args) {
        obj01 demo = new obj01();

        Dog dog = demo.new Dog("Friend");
        System.out.println("Dog's name is " + dog.getName());
        dog.rename("Best Friend");
        System.out.println("Dog's new name is " + dog.getName());
        dog.speak();
    }
}
