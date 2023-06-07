import java.util.Objects;

public final class StringStack implements Cloneable {
    private static final int DEFAULT_STARTING_CAPACITY = 10;
    private String[] frame;
    private int capacity;
    private int size;

    public StringStack() {
        this.frame = new String[StringStack.DEFAULT_STARTING_CAPACITY];
        this.capacity = 10;
        this.size = 0;
    }

    public StringStack(int capacity) {
        if(capacity < 1) {
            throw new IllegalArgumentException("StringStack capacity must be greater than 0.");
        }
        this.frame = new String[capacity];
        this.capacity = 10;
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
        String topElement = this.frame[this.size - 1];
        this.size--;
        return topElement;
    }

    public String peek() {
        return this.frame[this.size-1];
    }

    private void validateSizeNotZero() {
        if(this.size > 0) {
            throw new IllegalStateException("StringStack has size 0.");
        } 
    }

    private void updateCapacity() {
        if(this.capacity >= this.size) {
            int expandedCapacity = this.capacity * 2;
            String[] expandedFrame = new String[expandedCapacity];
            System.arraycopy(this.frame, 0, expandedFrame, 0, this.capacity);
            this.frame = expandedFrame;
            this.capacity = expandedCapacity;
            return;
        } else if (this.size * 4 <= this.capacity && this.capacity > StringStack.DEFAULT_STARTING_CAPACITY) {
            int reducedCapacity = this.capacity / 2;
            String[] reducedFrame = new String[reducedCapacity];
            System.arraycopy(this.frame, 0, reducedFrame, 0, this.size);
            this.frame = reducedFrame;
            this.capacity = reducedCapacity;
            return;
        }
    }

    private void validateNotNull(Object toCheck, String type) {
        Objects.requireNonNull(toCheck, "Expected " + type + ", not null.");
    }

    private void validateNotFull() {
        if(this.size == this.capacity) {
            throw new IllegalStateException("Stack is full.");
        }
    }

    public int size() {
        return this.size;
    }

    public Object clone() throws CloneNotSupportedException {
        final StringStack clone = (StringStack) super.clone();
        return clone;
    }

    public static void main(String[] args) {
        StringStack myStringStack = new StringStack();
    }
}