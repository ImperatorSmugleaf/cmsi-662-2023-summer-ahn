import java.util.Objects;

public final class StringStack implements Cloneable {
    // PRIVATE 
    private static final int DEFAULT_STARTING_CAPACITY = 10;
    private String[] frame;
    private int capacity;
    private int size;

    private void validateSizeNotZero() {
        if(this.isEmpty()) {
            throw new IllegalStateException("StringStack has size 0.");
        } 
    }

    private void updateCapacity() {
        int newCapacity = -1;
        if(this.capacity >= this.size + 1) {
            validateCanGrow();
            newCapacity = this.capacity * 2;
        } else if (this.size + 1 * 4 <= this.capacity && this.capacity > StringStack.DEFAULT_STARTING_CAPACITY) {
            newCapacity = this.capacity / 2;
        } else {
            return;
        }

        String[] newFrame = new String[newCapacity];
        System.arraycopy(this.frame, 0, newFrame, 0, this.frame.length);
        this.frame = newFrame;
        this.capacity = newCapacity;
    }

    private void validateNotNull(Object toCheck, String type) {
        Objects.requireNonNull(toCheck, "Expected " + type + ", not null.");
    }

    private void validateNotFull() {
        if(this.size + 1 >= this.capacity) {
            throw new IllegalStateException("Stack is full.");
        }
    }

    private int validatedCapacity(int capacity) {
        if(capacity < 2) {
            throw new IllegalArgumentException("Stack too small.");
        }

        if (capacity >= Integer.MAX_VALUE) {
            throw new IllegalArgumentException("Stack too large");
        }

        return capacity;
    }

    private void validateCanGrow() {
        if(this.capacity * 2 <= 0) {
            throw new IllegalStateException("Stack cannot grow any further");
        }
    }

    //PUBLIC
    public StringStack() {
        this.frame = new String[StringStack.DEFAULT_STARTING_CAPACITY];
        this.capacity = 10;
        this.size = 0;
    }

    public StringStack(int capacity) {
        int safeCapacity = this.validatedCapacity(capacity);
        this.frame = new String[safeCapacity];
        this.capacity = safeCapacity;
        this.size = 0;
    }

    public void push(String newElement) {
        this.validateNotNull(newElement, "string");
        this.validateNotFull();
        this.frame[this.size] = newElement;
        this.size++;
        this.updateCapacity();
    }

    public String pop() {
        this.validateSizeNotZero();
        this.size--;
        String topElement = this.frame[this.size];
        this.frame[this.size] = null;
        this.updateCapacity();
        return topElement;
    }

    public String peek() {
        return this.frame[this.size-1];
    }

    public int size() {
        return this.size;
    }

    public boolean isEmpty() {
        return this.size == 0;
    }

    public Object clone() throws CloneNotSupportedException {
        final StringStack clone = (StringStack) super.clone();
        return clone;
    }

    public static void main(String[] args) {
        StringStack myStringStack = new StringStack(100);
        System.out.println(myStringStack.isEmpty());
        myStringStack.push("Hello");
        myStringStack.push("World!");
        System.out.println(myStringStack.size());
        System.out.println(myStringStack.peek());
        System.out.println(myStringStack.isEmpty());
        var world = myStringStack.pop();
        System.out.println(myStringStack.peek());
        var hello = myStringStack.pop();
        System.out.println(hello + " " + world);
    }
}